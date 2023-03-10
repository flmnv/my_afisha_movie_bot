#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 11.03.2023, 01:12.

import logging

from aiogram import types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

from src.config import text, dp


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
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
