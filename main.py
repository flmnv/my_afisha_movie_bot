import logging

from aiogram import executor, types
from aiogram.dispatcher import Dispatcher
from src.commands import Commands

import src.config as config


async def bot_startup(dp: Dispatcher):
    dp.register_message_handler(Commands.start, commands=['start'])

    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Старт')
    ])


def main():
    try:
        config.startup()
        executor.start_polling(dispatcher=config.dp, on_startup=bot_startup)
    except BaseException as e:
        logging.error(e)


if __name__ == '__main__':
    main()
