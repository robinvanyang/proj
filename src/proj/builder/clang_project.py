import re

from proj.builder.project import Project
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

    def build_clang_project(self, language: LanguageType, project_type: ProjectType):
        render_datas = []
        direct_copy_file_list = []
        if language == self.LanguageType.C and project_type == self.ProjectType.STATIC:
            render_datas = [
                {
                    'tpl_file': 'CMakeLists.txt.jinja',
                    'render_data': {
                        'ProjectName': self.project_name
                    }
                },
                {
                    'tpl_file': 'imstaticlib.c.jinja',
                    'render_data': {
                        'ProjectName': self.project_name
                    },
                    'final_file': f'{self.project_name.lower()}.c',
                }
            ]

            direct_copy_file_list = [
                {
                    'tpl': 'imstaticlib.h.jinja',
                    'final': f'{self.project_name.lower()}.h'
                },
            ]

        if language == self.LanguageType.C and project_type == self.ProjectType.SHARED:
            split_words = re.sub(r"([A-Z])", r" \1", self.project_name).split()
            project_upper_symbol = '_'.join(list(map(lambda s: s.upper(), split_words)))

            render_datas = [
                {
                    'tpl_file': 'CMakeLists.txt.jinja',
                    'render_data': {
                        'ProjectName': self.project_name, 'ProjectUpperSymbol': project_upper_symbol
                    }
                },
                {
                    'tpl_file': 'imsharedlib.c.jinja',
                    'render_data': {
                        'ProjectName': self.project_name
                    },
                    'final_file': f'{self.project_name.lower()}.c',
                },
                {
                    'tpl_file': 'imsharedlib.h.jinja',
                    'render_data': {
                        'ProjectName': self.project_name, 'ProjectUpperSymbol': project_upper_symbol
                    },
                    'final_file': f'{self.project_name.lower()}.h',
                },
                {
                    'tpl_file': 'imsharedlib_export.h.jinja',
                    'render_data': {
                        'ProjectName': self.project_name, 'ProjectUpperSymbol': project_upper_symbol
                    },
                    'final_file': f'{self.project_name.lower()}_export.h',
                }
            ]

        self.render(f'{language.value}-{project_type.value}', render_datas, direct_copy_file_list)
        return ExitStatus.SUCCESS
