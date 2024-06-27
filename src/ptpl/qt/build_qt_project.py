import os
import shutil

from ptpl.status import ExitStatus
from jinja2 import Environment, FileSystemLoader, select_autoescape

from ptpl import utils
from pathlib import Path


def build_cmake_qt_app(project_name=None, window_name="MainWindow"):
    project_path = Path(os.path.join(os.getcwd(), project_name))
    project_path.mkdir(parents=True, exist_ok=True)
    os.chdir(project_path)

    template_path = os.path.join(utils.get_template_path(), "cmake-qt-app")
    print(template_path)

    env = Environment(loader=FileSystemLoader(template_path), autoescape=select_autoescape())

    template = env.get_template("CMakeLists.txt.jinja")
    content = template.render(ProjectName=project_name, WindowClassName=window_name)
    file = open('CMakeLists.txt', 'w')
    file.write(content)
    file.close()

    template = env.get_template("main.cpp.jinja")
    content = template.render(WindowClassName=window_name)
    file = open('main.cpp', 'w')
    file.write(content)
    file.close()

    template = env.get_template("mainwindow.cpp.jinja")
    content = template.render(WindowClassName=window_name)
    file = open(f'{window_name.lower()}.cpp', 'w')
    file.write(content)
    file.close()

    template = env.get_template("mainwindow.h.jinja")
    content = template.render(WindowClassName=window_name)
    file = open(f'{window_name.lower()}.h', 'w')
    file.write(content)
    file.close()

    template = env.get_template("mainwindow.ui.jinja")
    content = template.render(WindowClassName=window_name)
    file = open(f'{window_name.lower()}.ui', 'w')
    file.write(content)
    file.close()

    shutil.copyfile(os.path.join(template_path, 'qt.cmake'), './qt.cmake')
    shutil.copyfile(os.path.join(template_path, 'QtWindowApp.ico'), f'./{project_name}.ico')

    template = env.get_template("qtwindowapp.qrc.jinja")
    content = template.render(ProjectName=project_name)
    file = open(f'{project_name.lower()}.qrc', 'w')
    file.write(content)
    file.close()

    template = env.get_template("QtWindowApp.rc.jinja")
    content = template.render(ProjectName=project_name)
    file = open(f'{project_name}.rc', 'w')
    file.write(content)
    file.close()

    return ExitStatus.SUCCESS
