import aiohttp

from . import url, headers


async def get_all(day: int, mouth: int, year: int, name: str) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/cash-reports/{day}/{mouth}/{year}/{name}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None



async def create(data: dict) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.post(
                f'{url}/cash-reports',
                json=data
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None