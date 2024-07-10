import os
import typer
from typing_extensions import Annotated
from pathlib import Path
from proj.builder.qt_project import QtProject

new_proj = typer.Typer()


def check_project_name(project_name: str):
    project_path = Path(os.path.join(os.getcwd(), project_name))
    if project_path.is_dir():
        raise typer.BadParameter("Error: The project directory exist.")
    return project_name


@new_proj.command()
def qt(project_name: Annotated[str, typer.Option(callback=check_project_name, prompt="Please Input the Project Name:")],
       window_name: Annotated[str, typer.Option(prompt="Please Input the MainWindow Name:")], ):
    project_builder = QtProject(project_name)
    project_builder.build_qt_project(window_name)


@new_proj.command()
def clang():
    print("clang command")
