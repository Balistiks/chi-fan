import aiohttp

from . import url, headers


async def is_exist(tgId: int) -> str | bool:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            is_exist = await (await session.get(
                f'{url}/users/{tgId}/isExist'
            )).text()

            if is_exist == 'true':
                return True
            else:
                return False
        except aiohttp.client_exceptions.ContentTypeError:
            return False


async def get_functionals(tgId: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/users/{tgId}/functionals'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def get_by_tg_id(tg_id: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/users/{tg_id}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def save(user: dict) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.post(
                f'{url}/users',
                data=user
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def update(user: dict, tg_id: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.patch(
                f'{url}/users/{tg_id}',
                data=user
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None
