import aiohttp

from . import url, headers


async def get_by_id(point_id: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/revenues/{point_id}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def get_by_id_amount(id: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/revenues/amount/{id}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def get_all() -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/revenues/all'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None
