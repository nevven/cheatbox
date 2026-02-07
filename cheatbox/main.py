import typer
from typing import Optional

from .data import Data
from .display import Display

app = typer.Typer(help="Cheatbox - Cheatsheet in Bentobox", context_settings={"help_option_names" : ["-h", "--help"]})

@app.command()
def show(domain: str = typer.Argument(None, help="Cheatsheet to display (e.g., docker, linux, kubernetes)")):
    if domain is None:
        available = Data.list_domains()
        print("Available cheatsheets:", ", ".join(available))
        raise typer.Exit()

    data = Data(domain)
    if data.content:
        Display().display_bento(data.content)

if __name__ == "__main__":
    app()
