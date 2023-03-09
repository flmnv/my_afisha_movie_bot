#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 10.03.2023, 01:09.

import logging

from aiogram import types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

from src.config import text


class CommandStart:
    @staticmethod
    async def run(message: types.Message):
        try:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

            keyboard.add(
                KeyboardButton(text.commands.start.button_location, request_location=True)
            )

            await message.bot.send_message(
                message.chat.id,
                text.commands.start.message,
                reply_markup=keyboard
            )
        except BaseException as e:
            logging.error(e)
