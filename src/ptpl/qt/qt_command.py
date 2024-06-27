from cleo.commands.command import Command
from cleo.helpers import option
import ptpl.qt.build_qt_project as qt_project

from ptpl.status import ExitStatus


class QtCommand(Command):
    name = 'qt'
    description = 'Build Qt Project Template'
    options = [
        option(
            'project-name',
            flag=False
        ),
        # option(
        #     'build-tool',
        #     flag=False
        # ),
        option(
            'window-name',
            flag=False
        )
    ]

    def handle(self) -> int:
        project_name = self.option('project-name')
        if not project_name:
            project_name = self.ask('Please input project name:')

        window_name = self.option('window-name')
        if not window_name:
            window_name = self.ask('Please input window name:')

        qt_project.build_cmake_qt_app(project_name, window_name)
        return ExitStatus.SUCCESS
        pass
