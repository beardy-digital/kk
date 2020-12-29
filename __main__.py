import sys
from dependency_injector.wiring import Provide
from src.application import Application
from src.setup.ioc import Container


def main(action: str = None, verbose: bool = False, args=[], application: Application = Provide[Container.Application]):
    application.begin(action=action, verbose=verbose, args=args)


if __name__ == '__main__':
    container = Container()
    container.init_resources()
    container.wire(modules=[sys.modules[__name__]])
    args = sys.argv

    command = 'run'
    args = args[1:]
    if args[1] == 'search':
        command = 'search'
        args = args[2:]
    if args[1] == 'list':
        command = 'list'
        args = args[2:]
    main(action=command, args=args, verbose=False)
