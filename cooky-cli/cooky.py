import typer
from cmd.auth import auth_app

app = typer.Typer()

app.add_typer(auth_app, name="auth", help="Authentication provider for cooky")

if __name__ == '__main__':
    app()
