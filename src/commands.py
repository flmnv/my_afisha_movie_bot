from aiogram import types
import logging


def loggingerror(func):
    async def log(*args):
        try:
            await func(*args)
        except BaseException as e:
            logging.error(e)

    return log


class Commands:
    @staticmethod
    @loggingerror
    async def start(message: types.Message):
        await message.answer('Hi')
