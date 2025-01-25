import aiohttp

from . import url, headers


async def swap(first_id: int, second_id: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.patch(
                f'{url}/schedules/{first_id}/swap/{second_id}',
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None
