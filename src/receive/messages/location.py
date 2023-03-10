#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 11.03.2023, 01:12.

import logging

from aiogram import types

from src.api.open_weather.get_geo_reverse import GetGeoReverse
from src.config import dp


@dp.message_handler(content_types=['location'])
async def run(message: types.Message):
    try:
        geo_reverse = GetGeoReverse()
        response = await geo_reverse.get(message.location.latitude, message.location.longitude)

        await message.answer(
            f'{message.location.latitude} {message.location.longitude}'
            f'\nТвой город — {response.json[0]["name"]}'
        )
    except BaseException as e:
        logging.error(e)
