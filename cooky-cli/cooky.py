import typer
from cmd.auth import auth_app
from service.AuthService import AuthService
from dto.LoginRequestDTO import LoginRequestDTO

login_request_dto = LoginRequestDTO("stevanvlajic5@gmail.com", "stevanvlajic5")

AuthService().login(login_request_dto)

app = typer.Typer()

app.add_typer(auth_app, name="auth", help="Authentication provider for cooky")

if __name__ == '__main__':
    app()
