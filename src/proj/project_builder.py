import os
import shutil
from typing import List, Dict

from proj.status import ExitStatus
from jinja2 import Environment, FileSystemLoader, select_autoescape

from proj import utils
from pathlib import Path


class ProjectBuilder:
    def __init__(self, project_name: str):
        self.project_name = project_name

    def build_qt_project(self, window_name="MainWindow"):
        render_datas = [
            {
                'tpl_file': 'CMakeLists.txt.jinja',
                'render_data': {
                    'ProjectName': self.project_name, 'WindowClassName': window_name
                }
            },
            {
                'tpl_file': 'main.cpp.jinja',
                'render_data': {
                    'WindowClassName': window_name
                }
            },
            {
                'tpl_file': 'mainwindow.cpp.jinja',
                'render_data': {
                    'WindowClassName': window_name
                },
                'final_file': f'{window_name.lower()}.cpp',
            },
            {
                'tpl_file': 'mainwindow.h.jinja',
                'render_data': {
                    'WindowClassName': window_name
                },
                'final_file': f'{window_name.lower()}.h',
            },
            {
                'tpl_file': 'mainwindow.ui.jinja',
                'render_data': {
                    'WindowClassName': window_name
                },
                'final_file': f'{window_name.lower()}.ui',
            },
            {
                'tpl_file': 'qtwindowapp.qrc.jinja',
                'render_data': {
                    'ProjectName': self.project_name
                },
                'final_file': f'{self.project_name.lower()}.qrc',
            },
            {
                'tpl_file': 'QtWindowApp.rc.jinja',
                'render_data': {
                    'ProjectName': self.project_name
                },
                'final_file': f'{self.project_name.lower()}.rc',
            },
        ]

        direct_copy_file_list = [
            {
                'tpl': 'qt.cmake',
                'final': 'qt.cmake'
            },
            {
                'tpl': 'QtWindowApp.ico',
                'final': f'{self.project_name}.ico'
            }
        ]

        self.render('qt-project', render_datas, direct_copy_file_list)
        return ExitStatus.SUCCESS

    def render(self, project_type:str, render_datas: List[Dict], direct_copy_datas: List[Dict]):
        project_path = Path(os.path.join(os.getcwd(), self.project_name))
        project_path.mkdir(parents=True, exist_ok=True)
        os.chdir(project_path)

        template_path = os.path.join(utils.get_template_path(), project_type)
        env = Environment(loader=FileSystemLoader(template_path), autoescape=select_autoescape())

        for item in render_datas:
            template = env.get_template(item['tpl_file'])
            content = template.render(item['render_data'])

            if 'final_file' in item:
                final_file = item['final_file']
            else:
                final_file = Path(item['tpl_file']).stem
            file = open(final_file, 'w')

            file.write(content)
            file.close()

        for item in direct_copy_datas:
            shutil.copyfile(os.path.join(template_path, item['tpl']), item['final'])
