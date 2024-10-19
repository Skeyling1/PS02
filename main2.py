# Задание 2: Параметры запрос
# # 1. Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# # 2. Отправьте GET-запрос с параметром `userId`, равным `1`.
# # 3. Распечатайте полученные записи.

import requests
import pprint

parameter = {"userId" : 1}


result = requests.get('https://jsonplaceholder.typicode.com/posts', params=parameter, )

print(result.status_code)

pprint.pprint(result.json())