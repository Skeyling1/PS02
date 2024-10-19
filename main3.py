# Задание 3: Отправка данных
# # 1. Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# # 2. Создайте словарь с данными для отправки (например, `{'title': 'foo', 'body': 'bar', 'userId': 1}`).
# # 3. Отправьте POST-запрос с этими данными.
# # 4. Распечатайте статус-код и содержимое ответа.

import requests
import pprint

parameter = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}


result = requests.post('https://jsonplaceholder.typicode.com/posts', data=parameter, )

print(result.status_code)

pprint.pprint(result.json())