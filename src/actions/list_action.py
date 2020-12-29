from logging import Logger

from src.actions.action import Action
from src.actions.action_lists.action_list_loader import ActionListLoader


class ListAction(Action):
    def __init__(self,
                 action_list_loader: ActionListLoader,
                 logger: Logger):
        Action.__init__(self, logger)
        self.action_list_loader = action_list_loader

    def perform(self, verbose: bool = False):
        Action.perform(self)
        for item in self.action_list_loader.load():
            self.logger.info(item)

