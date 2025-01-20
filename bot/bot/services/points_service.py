import aiohttp

from . import url, headers


async def get_names():
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/points/names'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def get_all() -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/points/all'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None