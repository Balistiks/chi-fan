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


async def get_by_id(check_list_id: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/check-lists/{check_list_id}',
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None