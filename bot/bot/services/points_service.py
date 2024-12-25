import aiohttp

from . import url, headers


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


async def get_by_id_and_mouth(point_id: int, index_mouth: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/points/{point_id}/{index_mouth}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None