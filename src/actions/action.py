from logging import Logger
from typing import List


class Action:
    def __init__(self, logger: Logger):
        self.logger = logger

    def perform(self):
        self.logger.info(f'Action: {self.__class__.__name__}')
