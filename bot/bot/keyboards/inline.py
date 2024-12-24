from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

from bot.services import users_service


async def main_menu(tgId: int) -> InlineKeyboardMarkup:
    functionals = await users_service.get_functionals(tgId)
    buttons = []

    for functional in functionals:
        if functional['name'] == 'Мои смены':
            button = InlineKeyboardButton(text=functional['name'], web_app=WebAppInfo(url='https://chifan-corp.ru'))
        else:
            button = InlineKeyboardButton(text=functional['name'], callback_data=functional['callbackData'])
        buttons.append([button])

    buttons.append([InlineKeyboardButton(text='Задать вопрос', callback_data='question')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


