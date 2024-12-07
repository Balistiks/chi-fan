import aiohttp

from . import url, headers


async def get_all() -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/topics/first'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def get_by_id(topic_id: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/topics/{topic_id}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None