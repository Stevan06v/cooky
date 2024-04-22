from dataclasses import asdict

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
        url = "http://propromo.test/api/v1/users/login"
        login_response = requests.post(url, json=asdict(login_request_dto))
        login_response.raise_for_status()  # Raise HTTPError for non-200 status codes

        login_response_json = login_response.json()

        if not login_response_json.get("success"):
            raise CookyException("Invalid credentials!")

        return User.create_user_from_json(login_response_json)

    @staticmethod
    def register(register_request_dto):
        url = "http://propromo.test/api/v1/users"
        try:
            register_response = requests.post(url, json=asdict(register_request_dto))
            register_response_json = register_response.json()

            return User.create_user_from_json(register_response_json)
        except requests.exceptions.HTTPError as error:
            raise CookyException(error)

