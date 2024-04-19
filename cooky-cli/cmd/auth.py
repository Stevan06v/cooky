import typer
from typing_extensions import Annotated
from typing import Optional
from model.User import User
from manager.ConfigurationManager import ConfigurationManager
from service.AuthService import AuthService
from dto.LoginRequestDTO import LoginRequestDTO
from exception.CookyException import CookyException
from dto.RegisterRequestDTO import RegisterRequestDTO


auth_app = typer.Typer(name="Auth provider", help="Authentication provider.")


def login_with_dialog():
    typer.echo("Trying to log in with dialog..")


auth_app.command(name="login dialog", help="Log into your cooky account with a tui-dialog")(login_with_dialog)


def register_with_dialog():
    typer.echo("Trying to register in with dialog..")


auth_app.command(name="register dialog", help="Register cooky account with a tui-dialog")(login_with_dialog)


def login(email: Annotated[str, typer.Option("--email", "-e")],
          password: Annotated[str, typer.Option("--password", "-p")]):
    login_request_dto = LoginRequestDTO(email, password)

    try:
        user = AuthService().login(login_request_dto)
        ConfigurationManager().set_user_credentials(user)

        typer.echo(f"Successfully logged in with user {user.username}.")
    except CookyException as error:
        typer.echo(f"Cooky error: {error}")


auth_app.command(name="login", help="Log into your cooky account")(login)


def register(email: Annotated[str, typer.Option("--email", "-e")],
             password: Annotated[str, typer.Option("--password", "-p")],
             nickname: Annotated[Optional[str], typer.Option("--nickname", "-n")] = None):
    typer.echo("Trying to register..")
    register_request_dto = RegisterRequestDTO(email, password, nickname)

    try:
        user = AuthService().register(register_request_dto)
        ConfigurationManager().set_user_credentials(user)

        typer.echo(f"Successfully registered...")
    except CookyException as error:
        typer.echo(f"Cooky error: {error}")


auth_app.command(name="register", help="Create a cooky account.")(register)

