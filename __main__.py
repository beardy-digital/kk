import argparse
import sys
from dependency_injector.wiring import Provide
from src.application import Application
from src.setup.ioc import Container


def main(action: str = None, verbose: bool = False, args=[], application: Application = Provide[Container.Application]) -> None:
    application.begin(action=action, verbose=verbose, args=args)


if __name__ == '__main__':
    container = Container()
    container.init_resources()
    container.wire(modules=[sys.modules[__name__]])

    parser = argparse.ArgumentParser()
    parser.add_argument('list', nargs='?', help='List available commands')
    parser.add_argument('search', nargs='?', help='search')
    parser.add_argument('--verbose', help='verbose')
    args = parser.parse_args()

    action = ''
    verbose = False
    if args.__dict__['list']:
        action = 'list'
    if args.__dict__['verbose']:
        verbose = True

    main(action=action, verbose=verbose)
