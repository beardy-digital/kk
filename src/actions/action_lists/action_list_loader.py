from src.actions.action_lists.python_action_list import PythonActionList


class ActionListLoader:
    def __init__(self):
        self.action_list = [item for item in [PythonActionList()]]

    def load(self):
        for items_list in self.action_list:
            for item in items_list:
                yield item
