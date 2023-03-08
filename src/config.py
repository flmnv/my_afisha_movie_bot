import configparser
import logging
import os.path

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

import src.const as const

logging.basicConfig(
    level=logging.ERROR,
    filename='log.txt',
    format='%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
    datefmt='%H:%M:%S'
)

bot = None
storage = None
dp = None

config = configparser.ConfigParser()


def _load_config():
    if os.path.isfile('config.ini'):
        config.read('config.ini')
    else:
        with open('config.ini', 'w', encoding='utf-8') as config_file:
            config_file.write(const.CONFIG)


def _create_bot():
    global bot, storage, dp

    bot = Bot(token=config['TELEGRAM_BOT']['token'], parse_mode='html')
    storage = MemoryStorage()
    dp = Dispatcher(bot=bot, storage=storage)


def startup():
    try:
        _load_config()
        _create_bot()
    except BaseException as e:
        logging.error(e)
