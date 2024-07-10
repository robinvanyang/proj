from proj.builder.project import Project
from proj.status import ExitStatus


class QtProject(Project):
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
