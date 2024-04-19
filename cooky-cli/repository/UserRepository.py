from repository.IRepository import IRepository


class UserRepository(IRepository):
    def __init__(self):
        self.user = {}

    def get_all(self):
        pass

    def get_by_id(self, id):
        pass

    def create(self, item):
        pass

    def update(self, item):
        pass

    def delete(self, id):
        pass