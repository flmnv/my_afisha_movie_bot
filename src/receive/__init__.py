#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 11.03.2023, 01:12.

from glob import glob
from importlib import import_module
from os.path import dirname, basename, isfile, join


def load(folders: list):
    for folder in folders:
        modules = glob(join(dirname(__file__), fr'{folder}\*.py'))
        modules = ([basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')])

        for module in modules:
            import_module(f'{__name__}.{folder}.' + module)
