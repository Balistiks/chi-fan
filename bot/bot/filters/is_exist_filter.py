from aiogram import types
from aiogram.filters import Filter

from bot.services import users_service


class IsExistFilter(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return await users_service.is_exist(message.from_user.id)