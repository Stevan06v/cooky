from repository.IRepository import IRepository


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class RecipeRepository(IRepository):
    def __init__(self):
        self.recipes = []

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