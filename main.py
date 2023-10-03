from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import gspread

# Заголовок с юзер-агентом
headers = {
    'User-agent': UserAgent().random
}


def contract_html():
    # Запрос к странице с контрактом
    url_contract = input('Введите ссылку на контракт: ')
    response = requests.get(url=url_contract, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    # Сбор информации
    contract_number = soup.find('span', 'cardMainInfo__purchaseLink distancedText').text.strip()
    organization_name = soup.find('span', 'cardMainInfo__content').text.strip()
    price = soup.find('span', 'cardMainInfo__content cost').text.strip()[:-2]
    date_contract = soup.find('div', 'date mt-auto')
    start_date, end_date = [i.find('span', 'cardMainInfo__content').text.strip()
                            for i in date_contract.find_all('div', 'cardMainInfo__section')[:2]]
    return [organization_name, contract_number, start_date, end_date, price, '', url_contract]


# Наполнение таблицы Google
def google_sheet():
    gs = gspread.service_account(filename='credits.json')  # подключаем файл с ключами и пр.
    sheet = gs.open_by_key('https://docs.google.com/spreadsheets/d/*id таблицы*/')  # подключаем таблицу по ID
    worksheet = sheet.sheet1  # получаем первый лист
    worksheet.append_row(contract_html(), table_range='A1')  # вносим информацию в таблицу

    # форматирование ячеек
    worksheet.format(f'A{len(worksheet.get_all_values())}:G{len(worksheet.get_all_values())}', {
        "horizontalAlignment": "CENTER",
        "wrapStrategy": "LEGACY_WRAP",
        "textFormat": {
            "fontSize": 10
        }
    })


# Вызов функции
google_sheet()

# Запрос на повторное использование
while True:
    result = input('Хотите продолжить? (д / н) ').lower()
    if result != 'д':
        break
    google_sheet()