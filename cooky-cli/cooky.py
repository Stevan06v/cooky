import os
import typer
from cmd.auth import auth_app
from manager.ConfigurationManager import ConfigurationManager
from model.User import User

app = typer.Typer()

configManager = ConfigurationManager()

user = User(12, "stevanvlajic5", "stevanvlajic5@gmail.com", "Stevan-20060901!")
configManager.set_user_credentials(user)


app.add_typer(auth_app, name="auth", help="Authentication provider for cooky")

if __name__ == '__main__':
    app()
