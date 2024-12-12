from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


END_GPT_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Закончить диалог', callback_data='main_menu')
        ]
    ]
)

BACK_GPT_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='main_menu')
        ]
    ]
)