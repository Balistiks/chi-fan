import aiohttp

from . import url, headers


async def is_exist(name: str) -> bool:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/names/{name}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None