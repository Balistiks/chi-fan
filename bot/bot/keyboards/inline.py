from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.services import users_service


async def main_menu(tgId: int) -> InlineKeyboardMarkup:
    functionals = await users_service.get_functionals(tgId)
    buttons = []

    for functional in functionals:
        button = InlineKeyboardButton(text=functional['name'], callback_data=functional['callbackData'])
        buttons.append([button])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


