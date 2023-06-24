import requests
from bs4 import BeautifulSoup as bs
import gspread
import fake_useragent

# Заголовок с юзер-агентом
headers = {
    'User-agent': fake_useragent.UserAgent().random
}

# Ссылка на контракт
url_contract = input('Введите ссылку на контракт: ')

def parsing_contract(adress):
    # Получение кода страницы
    response = requests.get(url=adress, headers=headers).text
    soup = bs(response, 'lxml')

    # Название организации и цена на контракт
    organization_name = soup.find('span', class_='cardMainInfo__content').find('a').get_text().strip()
    price = soup.find('span', class_='cardMainInfo__content cost').get_text().strip()[:-2]

    # Дата заключение и исполнения контракта
    block_data = soup.find('div', class_='date mt-auto')
    start_data = block_data.find('span', class_='cardMainInfo__content').get_text().strip()
    end_data = block_data.find_all('span')[3].text.strip()

    # Номер контракта
    block_contract = soup.find('div', class_='sectionMainInfo__body')
    a = block_contract.find_all('div')[1].find('span', class_='cardMainInfo__content').text.strip().split('\n')
    contract = a[0] + a[-1].strip()
    # Наполнение таблицы Google
    gs = gspread.service_account(filename='credits.json')  # подключаем файл с ключами и пр.
    sheet = gs.open_by_key('Введите id таблицы')  # подключаем таблицу по ID
    worksheet = sheet.sheet1  # получаем первый лист
    rows = [organization_name, contract, start_data, end_data, price, '', url_contract]
    worksheet.append_row(rows, table_range='A1')

    #форматирование ячеек
    worksheet.format(f'A{len(worksheet.get_all_values())}:G{len(worksheet.get_all_values())}', {
        "backgroundColor": {
            "red": 0,
            "green": 139,
            "blue": 139
        },
        "horizontalAlignment": "CENTER",
        "wrapStrategy": "LEGACY_WRAP",
        "textFormat": {
            "foregroundColor": {
                "red": 1.0,
                "green": 1.0,
                "blue": 1.0
            },
            "fontSize": 12
        }
    })

# Вызов функции
parsing_contract(url_contract)

# Запрос на повторное использование
while True:
    result = input('Хотите продолжить? (д / н) ').lower()
    if result != 'д':
        break
    URL_TEMPLATE = input('Введите ссылку на контракт: ')
    parsing_contract(url_contract)