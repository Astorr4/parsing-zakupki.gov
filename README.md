Данный скрипт предназначен для парсинга данных из реестра контрактов zakupki.gov.ru

Для начала работы необходимо:
1. Создать и настроить google проект (https://console.cloud.google.com/)
2. После создания и первичной настройки к проекту необходимо подключить API (Google Drive API и Google sheets API)
3. Затем необходимо создать сервисный аккаунт с ролью редактора и скачать необходимые ключи в формате json
4. Файл с ключами необходимо поместить в папку со скриптом и переименовать его в "credits.json"
5. В созданной google таблице необходимо дать доступ редактора нашему сервисному аккаунту
6. В коде, в переменную "sheet" вставить id таблицы (https://docs.google.com/spreadsheets/d/*id таблицы*/)
7. На вход программе подается ссылка на контракт (пример: https://zakupki.gov.ru/epz/contract/contractCard/common-info.html?reestrNumber=3027707325623000007)
8. Пример таблицы для скрипта (https://docs.google.com/spreadsheets/d/10xvLTGru-uV67wMnEH7-M-wP2ZMSKXSRZB_64UgkT68/)
