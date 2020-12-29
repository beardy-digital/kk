from src.actions.action_lists.default_action_list import DefaultActionList


class PythonActionList(DefaultActionList):

    action_list = [{
        'name': 'python3.9',
        'command': 'docker run python:3.9-alpine %'
    }, {
        'name': 'python3.8.6',
        'command': 'docker run python:3.8-alpine %'
    }]

    def __init__(self):
        super().__init__()
        for action in self.action_list:
            self.append(action)
