import requests
import configuration
import data

def post_new_user(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_USER_API_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);
#response = post_new_user(data.headers);
print(response.status_code)

#{"authToken": "027bd3f8-4bea-45e1-a815-a9db27cc4ff8"}
#def get_auth_token():
#    return requests.get(configuration.BASE_URL + configuration.CREATE_USER_API_PATH, json=get_auth_token())
#response=get_auth_token();
#print(response.json())
#def post_new_client_kit(id, token):
#    return requests.post(configuration.BASE_URL + configuration.CREATE_KIT_API_PATH + id, headers = { "Cookie": "token=" + token})