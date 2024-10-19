#Задание 1: Получение данных
# Импортируйте библиотеку requests.
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

parameter = {"q" : "html"}


result = requests.get('https://api.github.com/search/repositories', params=parameter)

print(result.status_code)
print(result.url)
pprint.pprint(result.json())