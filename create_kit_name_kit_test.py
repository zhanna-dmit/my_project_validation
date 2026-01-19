import data
import configuration
import requests
import sender_stand_request


# Функция для получения нового токена через создание пользователя
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]


# Функция для генерации тела набора с разными name
def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body


# Позитивная проверка
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201, f"Ожидался код 201, а пришёл {response.status_code}"
    assert response.json()["name"] == kit_body["name"], "Поле name в ответе не совпадает с запросом"


# Негативная проверка (код 400)
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400, f"Ожидался код 400, а пришёл {response.status_code}"


# Тесты

def test_kit_name_1_char():
    positive_assert(get_kit_body("a"))

def test_kit_name_511_chars():
    positive_assert(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"))

def test_kit_name_0_chars():
    negative_assert_code_400(get_kit_body(""))

def test_kit_name_512_chars():
    negative_assert_code_400(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"))

def test_kit_name_english_letters():
    positive_assert(get_kit_body("QWErty"))

def test_kit_name_russian_letters():
    positive_assert(get_kit_body("Мария"))

def test_kit_name_special_symbols():
    positive_assert(get_kit_body("№%@,"))

def test_kit_name_spaces():
    positive_assert(get_kit_body(" Человек и КО "))

def test_kit_name_digits():
    positive_assert(get_kit_body("123"))

def test_kit_name_missing_param():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

def test_kit_name_wrong_type_number():
    kit_body = data.kit_body.copy()
    kit_body["name"] = 123
    negative_assert_code_400(kit_body)
