import os
from dotenv import load_dotenv
from pathlib import Path
import configparser


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class ConfigurationManager:
    def __init__(self):
        dotenv_path = Path('.env')
        load_dotenv(dotenv_path=dotenv_path)

        self.config = configparser.ConfigParser()
        self.config_path = os.getenv('CONFIG_FILE_PATH')

        self.load_config_file()

    def load_config_file(self):
        if os.path.exists(self.config_path):
            self.config.read(self.config_path)
        else:
            self.config['DEFAULT'] = {}

    def set_user_auth_token(self, auth_token):
        self.config['AUTHENTICATION']['APP_TOKEN'] = auth_token
        self.save_config_file()

    def set_user_credentials(self, user):
        self.config['AUTHENTICATION']['EMAIL'] = user.email
        self.config['AUTHENTICATION']['NICKNAME'] = user.nickname

        self.save_config_file()

    def save_config_file(self):
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)
