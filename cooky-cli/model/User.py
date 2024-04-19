class User:
    def __init__(self, _id, _nickname, _email, _password):
        self.id = _id
        self.nickname = _nickname
        self.email = _email
        self.password = _password

    @staticmethod
    def create_from_response(user_response):
        return NotImplementedError

