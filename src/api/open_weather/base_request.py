#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 11.03.2023, 01:12.

import aiohttp

import src.config as config
from src.api.open_weather.response import Response


class BaseRequest:
    def __init__(self):
        self.host = config.ini['API_OPEN_WEATHER']['host']
        self.endpoint = config.ini['API_OPEN_WEATHER']['endpoint']
        self.key = config.ini['API_OPEN_WEATHER']['key']

        self.response = None
        self.json = None

    async def _get(self, url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.host + self.endpoint + url) as response:
                return Response(response.status, await response.json())
