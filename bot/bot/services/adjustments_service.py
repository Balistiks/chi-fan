import aiohttp

from . import url, headers


async def get_all_by_names(point: str, name: str, index: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/adjustments/{point}/{name}/{index}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None