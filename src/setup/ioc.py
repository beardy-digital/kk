from src.setup.logging_handler import configure as logging_configuration
from src.application import Application
from src.actions.search_action import SearchAction
from src.actions.run_action import RunAction
from src.actions.list_action import ListAction
from src.actions.action_lists.action_list_loader import ActionListLoader
from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    Logger = providers.Singleton(logging_configuration)
    config = providers.Configuration()

    ActionListLoader = providers.Singleton(
        ActionListLoader,

    )

    SearchAction = providers.Singleton(
        SearchAction,
        Logger
    )
    RunAction = providers.Singleton(
        RunAction,
        Logger
    )
    ListAction = providers.Singleton(
        ListAction,
        ActionListLoader,
        Logger
    )

    Application = providers.Singleton(
        Application,
        SearchAction,
        ListAction,
        RunAction
    )
