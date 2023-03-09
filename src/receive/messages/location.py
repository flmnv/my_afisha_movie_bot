#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 10.03.2023, 01:10.

import logging

from aiogram import types

from src.api.open_weather.get_geo_reverse import GetGeoReverse


class MessageLocation:
    @staticmethod
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
