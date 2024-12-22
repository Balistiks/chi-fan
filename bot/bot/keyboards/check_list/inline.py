import math

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder



async def check_list_keyboard(check_list: list, current_page: int) -> InlineKeyboardMarkup:
    total_pages = math.ceil(len(check_list) / 6)

    start_index = current_page * 6
    end_index = start_index + 6
    page_items = check_list[start_index:end_index]

    buttons = []
    for index, point_check_list in enumerate(page_items):
        buttons.append([InlineKeyboardButton(text=point_check_list, callback_data=f'check_list_{start_index + index}')])

    prev_callback_data = f'check_list-prev_page_{current_page - 1}' if current_page > 0 else '#'
    next_callback_data = f'check_list-next_page_{current_page + 1}' if current_page < total_pages - 1 else '#'

    navigation_buttons = [
        InlineKeyboardButton(text='⬅️', callback_data=prev_callback_data),
        InlineKeyboardButton(text=f'{current_page + 1}/{total_pages}', callback_data='#'),
        InlineKeyboardButton(text='➡️', callback_data=next_callback_data)
    ]

    buttons.append(navigation_buttons)

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


CONFIRM_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Подтвердить', callback_data='check_list-confirm'),
        ]
    ]
)

PHOTO_ADD_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Прикрепить', callback_data='check_list-add_photo'),
        ]
    ]
)

PHOTO_CONFIRM_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Подтвердить', callback_data='check_list-confirm'),
        ],
        [
            InlineKeyboardButton(text='Прикрепить', callback_data='check_list-add_photo'),
        ]
    ]
)



