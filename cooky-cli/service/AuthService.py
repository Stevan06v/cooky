import requests
from model.User import User
from exception.CookyException import CookyException


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class AuthService:
    @staticmethod
    def login(login_request_dto):
        url = "http://cooky-rest/api/v1/login"
        try:
            login_response = requests.post(url, json=login_request_dto)
            post_response_json = login_response.json()

            return User.create_user_from_response(post_response_json)
        except requests.exceptions.HTTPError as error:
            raise CookyException(error)

    @staticmethod
    def register(register_request_dto):
        url = "http://cooky-rest/api/v1/register"
        try:
            register_response = requests.post(url, json=register_request_dto)
            register_response_json = register_response.json()

            return User.create_user_from_response(register_response_json)
        except requests.exceptions.HTTPError as error:
            raise CookyException(error)

