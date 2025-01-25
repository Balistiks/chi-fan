from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

SWAP_NO_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мои смены', callback_data='#'),
        ],
        [
            InlineKeyboardButton(text='Вернуть в главное меню', callback_data='main_menu'),
        ],
    ]
)