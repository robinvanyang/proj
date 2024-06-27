from ptpl.qt.qt_command import QtCommand
from cleo.application import Application


def main():
    app = Application()
    app.add(QtCommand())
    app.run()
