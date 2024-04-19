import typer
from typing_extensions import Annotated


manager_app = typer.Typer(name="cookbook", help="Manage your recipes")


def add_recipe(name: Annotated[str, typer.Option("--name", )]):
    print("Adding recipe")


manager_app.command(name="add-recipe", help="Add your recipes")(add_recipe)


