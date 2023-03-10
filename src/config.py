#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 14.03.2023, 23:24.

import configparser
import json
import logging
import os.path
import typing
from pathlib import Path
from types import SimpleNamespace

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

import src.const as const

logging.basicConfig(
    level=logging.ERROR,
    filename='log.txt',
    format='%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

bot: typing.Union[Bot, None] = None
storage: typing.Union[MemoryStorage, None] = None
dp: typing.Union[Dispatcher, None] = None

ini = configparser.ConfigParser()
text = None


def logerror(func):
    def log(*args):
        try:
            func(*args)
        except BaseException as e:
            logging.error(e)
            exit(1)

    return log


@logerror
def _load_config():
    if os.path.isfile('config.ini'):
        ini.read('config.ini')
    else:
        with open('config.ini', 'w', encoding='utf-8') as config_file:
            config_file.write(const.CONFIG)


@logerror
def _load_json():
    global text

    with open(Path('json', 'text.json'), 'r', encoding='utf-8') as json_file:
        text = json.load(json_file, object_hook=lambda d: SimpleNamespace(**d))


@logerror
def _create_bot():
    global bot, storage, dp

    bot = Bot(token=ini['API_TELEGRAM']['token'], parse_mode='html')
    storage = MemoryStorage()
    dp = Dispatcher(bot=bot, storage=storage)


def startup():
    _load_config()
    _load_json()
    _create_bot()
