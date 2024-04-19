import json
from dataclasses import dataclass


@dataclass
class User:
    def __init__(self, _id, _nickname, _email):
        self.id = _id
        self.nickname = _nickname
        self.email = _email

    @staticmethod
    def create_user_from_response(response):
        data = json.loads(response)
        user = User(**data)
        return user
