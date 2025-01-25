from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

SWAP_NO_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мои смены', web_app=WebAppInfo(url='https://chifan-corp.ru')),
        ],
        [
            InlineKeyboardButton(text='Вернуть в главное меню', callback_data='main_menu'),
        ],
    ]
)