import aiohttp

from . import url, headers


async def get_months(employee_name: str):
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/salaries/months/{employee_name}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def get_names_points(employee_name: str, month: str):
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/salaries/points/{month}/{employee_name}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def get_by_name_point_employee_name(employee_name: str, mouth: str) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/salaries/{employee_name}/{mouth}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def get_sums(name_point: str, employee_name: str, mouth: str) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/salaries/sum/{name_point}/{employee_name}/{mouth}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None


async def get_by_id(salary_id: int) -> dict | None:
    async with aiohttp.ClientSession(
        headers=headers
    ) as session:
        try:
            return await (await session.get(
                f'{url}/salaries/{salary_id}'
            )).json()
        except aiohttp.client_exceptions.ContentTypeError:
            return None