#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 11.03.2023, 01:16.

import logging

from aiogram import executor, types
from aiogram.dispatcher import Dispatcher

import src.config as config
import src.receive as receive


async def bot_startup(dp: Dispatcher):
    receive.load(['commands', 'messages'])

    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Старт')
    ])


def main():
    try:
        config.startup()
        executor.start_polling(dispatcher=config.dp, on_startup=bot_startup)
    except BaseException as e:
        logging.error(e)
        exit(1)


if __name__ == '__main__':
    main()
