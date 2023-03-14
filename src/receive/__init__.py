#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 14.03.2023, 23:24.

from importlib import import_module
from os.path import dirname
from pathlib import Path


def load(folders: list):
    for folder in folders:
        modules = Path(dirname(__file__), folder).glob('*.py')
        modules = [f.stem for f in modules if f.is_file() and not f.name.endswith('__init__.py')]

        for module in modules:
            import_module(f'{__name__}.{folder}.' + module)
