import json
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class User:
    id: int
    nickname: str
    email: str
    name: str

    @staticmethod
    def create_user_from_json(login_response_json):
        filtered_data = {
            'id': login_response_json['user']['id'],
            'name': login_response_json['user']['name'],
            'nickname': login_response_json['user']['nickname'],
            'email': login_response_json['user']['email']
        }
        return User(**filtered_data)
