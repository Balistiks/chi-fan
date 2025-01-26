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


async def get_by_id(check_list_answer_id: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/check-list-answers/{check_list_answer_id}',
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None