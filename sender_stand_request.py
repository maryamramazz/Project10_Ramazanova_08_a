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


def post_new_client_kit(kit_body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_KIT_API_PATH,
                         json=kit_body,
                         headers=data.headers)
response = post_new_client_kit(data.kit_body);
#print(response.status_code)
