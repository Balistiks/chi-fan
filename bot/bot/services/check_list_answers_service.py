import aiohttp

from . import url, headers


async def create(check_list_answer: dict) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        return await (await session.post(
            f'{url}/check-list-answers',
            data=check_list_answer
        )).json()