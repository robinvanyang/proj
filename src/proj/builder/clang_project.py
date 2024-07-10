from proj.builder.project_builder import Project
from proj.status import ExitStatus
from enum import Enum


class CLangProject(Project):
    class LanguageType(str, Enum):
        C = "c"
        CXX = "cxx"

    class ProjectType(str, Enum):
        STATIC = "static"
        SHARED = "shared"
        APPLICATION = "application"

    def build_clang_project(self, language: LanguageType, type: ProjectType):
        render_datas = [
            {
                'tpl_file': 'mainwindow.cpp.jinja',
                'render_data': {
                    'WindowClassName': window_name
                },
                'final_file': f'{window_name.lower()}.cpp',
            },
        ]

        direct_copy_file_list = [
            {
                'tpl': 'qt.cmake',
                'final': 'qt.cmake'
            },
        ]

        self.render(f'{language.value}-{type.value}', render_datas, direct_copy_file_list)
        return ExitStatus.SUCCESS
