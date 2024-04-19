import typer
from typing_extensions import Annotated


auth_app = typer.Typer(name="Auth provider", help="Authentication provider.")


def login_with_dialog():
    typer.echo("Trying to log in with dialog..")


auth_app.command(name="login dialog", help="Log into your cooky account with a tui-dialog")(login_with_dialog)


def login(email: Annotated[str, typer.Option("--email", "-e")],
          password: Annotated[str, typer.Option("--password", "-p")]):
    typer.echo(f"Logging into {email}...")


auth_app.command(name="login", help="Log into your cooky account")(login)


def register():
    typer.echo("Trying to register..")


auth_app.command(name="register", help="Create a cooky account.")(register)

