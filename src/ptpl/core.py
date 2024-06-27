import os
import argparse
import shutil
from typing import AnyStr

import click
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
    print('build_cmake_qt_app')
    return ExitStatus.SUCCESS


def main():
    try:
        exit_status = ptpl()
    except KeyboardInterrupt:
        from ptpl.status import ExitStatus
        exit_status = ExitStatus.ERROR_CTRL_C

    return exit_status.value


if __name__ == '__main__':
    main()
