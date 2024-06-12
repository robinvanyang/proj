import os
import argparse
import shutil
from typing import AnyStr

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .status import ExitStatus
from rvy import pathutils


def ptpl():
    parser = argparse.ArgumentParser(description="Project Template Generator.")
    parser.add_argument('-t', '--template', required=True, help='Template project name')
    parser.add_argument('-vals', '--vals', required=False, nargs='+', help='List of values')

    args = parser.parse_args()
    print('parsed args:')
    print(f'template={args.template}')
    print(f'vals={args.vals}')

    match args.template:
        case "cmake-qt-app":
            status = build_cmake_qt_app()
        case _:
            status = ExitStatus.ERROR_UNDEFINED_TEMPLATE

    return status


def build_cmake_qt_app(project_name=None, window_name="MainWindow"):
    if project_name is None:
        project_name = pathutils.get_current_folder_name()

    template_path = os.path.join(get_template_path(), "cmake-qt-app")
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


def get_script_path() -> AnyStr:
    script_path = os.path.split(os.path.realpath(__file__))[0]
    return script_path


def get_template_path() -> AnyStr:
    return os.path.join(get_script_path(), "tpl")


def main():
    try:
        exit_status = ptpl()
    except KeyboardInterrupt:
        from ptpl.status import ExitStatus
        exit_status = ExitStatus.ERROR_CTRL_C

    return exit_status.value


if __name__ == '__main__':
    main()
