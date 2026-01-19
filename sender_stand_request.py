# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data 

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body)

def post_new_client_kit(kit_body, auth_token):
    # Создаём копию тела запроса, чтобы не менять исходные данные из data.py
    kit_body = kit_body.copy()

    # Заголовки с токеном авторизации
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }

    # Отправляем POST-запрос
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_KITS,
        json=kit_body,
        headers=headers
    )

# Вызов функции с данными из data.py
response = post_new_client_kit(data.kit_body, data.auth_token)

print(response.status_code)
print(response.json())