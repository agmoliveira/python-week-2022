import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beer_from_database

main = typer.Typer(help="Beer Managment application")


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database."""  
    if add_beer_to_database (name,style,flavor,image,cost):
        print("Beer was add")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """List the beers from database."""
    beers= get_beer_from_database()
    print(beers)
