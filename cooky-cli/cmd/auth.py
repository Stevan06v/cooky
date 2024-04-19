import typer
from typing_extensions import Annotated
from typing import Optional
from manager.ConfigurationManager import ConfigurationManager
from service.AuthService import AuthService
from dto.LoginRequestDTO import LoginRequestDTO
from exception.CookyException import CookyException
from dto.RegisterRequestDTO import RegisterRequestDTO
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.spinner import Spinner

console = Console()

auth_app = typer.Typer(name="Auth provider", help="Authentication provider.")


def login_with_dialog():
    typer.echo("Trying to log in with dialog..")


auth_app.command(name="login dialog", help="Log into your cooky account with a tui-dialog")(login_with_dialog)


def register_with_dialog():
    typer.echo("Trying to register in with dialog..")


auth_app.command(name="register dialog", help="Register cooky account with a tui-dialog")(login_with_dialog)


def login(email: str = typer.Option(..., "--email", "-e"),
          password: str = typer.Option(..., "--password", "-p")):
    with Live(
        Spinner("arc", text=Text("Logging into application...", style="white")),
        refresh_per_second=20,
    ) as live:
        live.start()

        login_request_dto = LoginRequestDTO(email, password)

        try:
            user = AuthService().login(login_request_dto)
            ConfigurationManager().set_user_credentials(user)
            live.stop()
            print(Panel("[bold green]Successfully logged in into cooky![/bold green]", style="green", title="Success",
                        title_align="left"))
        except Exception as error:
            live.stop()
            print(Panel(f"[bold red]An Error occurred: {error}[/bold red]", style="red", title="Exception",
                        title_align="left"))
            return


auth_app.command(name="login", help="Log into your cooky account")(login)


def register(email: Annotated[str, typer.Option("--email", "-e")],
             password: Annotated[str, typer.Option("--password", "-p")],
             nickname: Annotated[Optional[str], typer.Option("--nickname", "-n")]):
    typer.echo("Trying to register..")
    register_request_dto = RegisterRequestDTO(email, password, nickname)

    try:
        user = AuthService().register(register_request_dto)
        ConfigurationManager().set_user_credentials(user)

        print(f"Hello, [bold magenta]{user.nickname}[/bold magenta]! You are successfully registered!")
    except CookyException as error:
        typer.echo(f"Cooky error: {error.message}")


auth_app.command(name="register", help="Create a cooky account.")(register)

