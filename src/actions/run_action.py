import subprocess
from logging import Logger
from typing import List

from src.actions.action import Action


class RunAction(Action):
    def __init__(self, logger: Logger):
        Action.__init__(self, logger)

    def perform(self, command, args: List[str], verbose: bool):
        Action.perform(self)
        bash_command = f'{command}'
        arg_string = ''
        for arg in args:
            arg_string += f' {arg}'
        bash_command = bash_command.replace('%', arg_string)
        print(bash_command)
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)