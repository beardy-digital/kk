from logging import Logger

from src.actions.action import Action


class RunAction(Action):
    def __init__(self, logger: Logger):
        Action.__init__(self, logger)
