import json
from dataclasses import dataclass, asdict


@dataclass
class LoginRequestDTO:
    email: str
    password: str

    def to_json(self):
        return json.dumps(asdict(self))

