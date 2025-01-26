import aiohttp

from . import url, headers


async def get_by_name(name: str) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/users/byName/{name}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None