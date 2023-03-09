from src.api.open_weather.base_request import BaseRequest

LIMIT = 5


class GetGeoReverse(BaseRequest):
    def __init__(self):
        super().__init__()

    async def get(self, latitude: float, longitude: float):
        return await self._get(
            f'geo/1.0/reverse?lat={latitude}&lon={longitude}&limit={LIMIT}&appid={self.api_key}')