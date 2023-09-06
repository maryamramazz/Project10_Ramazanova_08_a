import sender_stand_request
import data
import configuration

#Функция для получения нового токена
def get_new_user_token():
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    return user_response.json()["authToken"]
response = get_new_user_token()
print(response)
#Функция на обновление токена
#def get_new_user_token():
#    global user_token
#    if user_token is None:
#        user_token = create_new_user()
#        return user_token
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

#Тест №1: Допустимое количество символов (1)
def positive_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]
def test_name_one_symbol():
    positive_assert("а")