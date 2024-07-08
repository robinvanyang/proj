import typer
from typing_extensions import Annotated
from proj.project_builder import ProjectBuilder

new_proj = typer.Typer()


@new_proj.command()
def qt(project_name: Annotated[str, typer.Option()], window_name: Annotated[str, typer.Option()]):
    project_builder = ProjectBuilder(project_name)
    project_builder.build_qt_project(window_name)


@new_proj.command()
def clang():
    print("clang command")
