import typer
import importlib.metadata
from rich import print
from proj.console.command_new import new_proj

app = typer.Typer()
app.add_typer(new_proj, name="new")


@app.command()
def version():
    _version = importlib.metadata.version('proj')
    print(_version)


def main():
    app()
