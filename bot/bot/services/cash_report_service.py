import aiohttp

from . import url, headers


async def get_all() -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/cash-reports'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def update(data: dict) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.patch(
                f'{url}/cash-reports',
                data=data
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None