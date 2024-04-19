import json
from dataclasses import dataclass, asdict


@dataclass
class RegisterRequestDTO:
    email: str
    password: str
    nickname: str

    def to_json(self):
        return json.dumps(asdict(self))
