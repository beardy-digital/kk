from logging import Logger
from typing import List

from src.actions.action import Action


class SearchAction(Action):
    def __init__(self, logger: Logger):
        Action.__init__(self, logger)

    def perform(self, args: List[str], verbose: bool = False):
        Action.perform(self)
