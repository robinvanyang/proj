import unittest
from ptpl.qt.qt_command import QtCommand
from cleo.application import Application
from cleo.testers.command_tester import CommandTester


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_example(self):
        application = Application()
        application.add(QtCommand())

        command = application.find("qt")
        command_tester = CommandTester(command)
        command_tester.execute('--project-name=SampleQtProject')

        output = command_tester.io.fetch_output()

        self.assertIn("SampleQtProject", output)


if __name__ == '__main__':
    unittest.main()
