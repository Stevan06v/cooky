import typer
from typing_extensions import Annotated
from typing import Optional
from model.User import User
from manager.ConfigurationManager import ConfigurationManager

auth_app = typer.Typer(name="Auth provider", help="Authentication provider.")


def login_with_dialog():
    typer.echo("Trying to log in with dialog..")


auth_app.command(name="login dialog", help="Log into your cooky account with a tui-dialog")(login_with_dialog)


def register_with_dialog():
    typer.echo("Trying to register in with dialog..")


auth_app.command(name="register dialog", help="Register cooky account with a tui-dialog")(login_with_dialog)


def login(email: Annotated[str, typer.Option("--email", "-e")],
          password: Annotated[str, typer.Option("--password", "-p")]):

    user = User(1, "hallo", email, password)

    ConfigurationManager().set_user_credentials(user)

    typer.echo(f"Logging into {email}...")


auth_app.command(name="login", help="Log into your cooky account")(login)


def register(email: Annotated[str, typer.Option("--email", "-e")],
             password: Annotated[str, typer.Option("--password", "-p")],
             nickname: Annotated[Optional[str], typer.Option("--nickname", "-n")] = None):
    typer.echo("Trying to register..")

    user = User(1, nickname, email, password)
    ConfigurationManager().set_user_credentials(user)


auth_app.command(name="register", help="Create a cooky account.")(register)

