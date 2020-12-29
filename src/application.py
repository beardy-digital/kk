from src.actions.action_lists.action_list_loader import ActionListLoader
from src.actions.list_action import ListAction
from src.actions.run_action import RunAction
from src.actions.search_action import SearchAction


class Application:
    def __init__(self,
                 search_action: SearchAction,
                 list_action: ListAction,
                 run_action: RunAction):
        self.search_action = search_action
        self.list_action = list_action
        self.run_action = run_action

    def begin(self, action, args, verbose):
        if action == 'search':
            return self.search(args, verbose)
        if action == 'list':
            return self.list(verbose)

        return self.run(args[0], args[1:], verbose)

    def search(self, args, verbose):
        return self.search_action.perform(args, verbose)

    def list(self, verbose):
        return self.list_action.perform(verbose)

    def run(self, command, args, verbose):
        for item in ActionListLoader().load():
            if item['name'] == command:
                print(command)
                return self.run_action.perform(item['command'], args, verbose)

        exit(1)
