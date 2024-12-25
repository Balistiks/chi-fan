import aiohttp

from . import url, headers


async def create(check_list: dict) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        return await (await session.post(
            f'{url}/check-lists',
            data=check_list
        )).json()