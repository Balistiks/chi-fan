import math
from datetime import datetime

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.services import points_service


async def points_keyboard() -> InlineKeyboardMarkup:
    points = await points_service.get_all()
    buttons = []

    for point in points:
        button = InlineKeyboardButton(text=point['name'], callback_data=f'check_id-{point['id']}')
        buttons.append([button])

    buttons.append([InlineKeyboardButton(text='Назад', callback_data='main_menu')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


MOUNTHS_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Январь', callback_data='check-1'),
        ],
        [
            InlineKeyboardButton(text='Февраль', callback_data='check-2'),
        ],
        [
            InlineKeyboardButton(text='Март', callback_data='check-3'),
        ],
        [
            InlineKeyboardButton(text='Апрель', callback_data='check-4'),
        ],
        [
            InlineKeyboardButton(text='Май', callback_data='check-5'),
        ],
        [
            InlineKeyboardButton(text='Июнь', callback_data='check-6'),
        ],
        [
            InlineKeyboardButton(text='Июль', callback_data='check-7'),
        ],
        [
            InlineKeyboardButton(text='Август', callback_data='check-8'),
        ],
        [
            InlineKeyboardButton(text='Сентябрь', callback_data='check-9'),
        ],
        [
            InlineKeyboardButton(text='Октябрь', callback_data='check-10'),
        ],
        [
            InlineKeyboardButton(text='Ноябрь', callback_data='check-11'),
        ],
        [
            InlineKeyboardButton(text='Декабрь', callback_data='check-12'),
        ],
        [
            InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu'),
        ],
    ]
)


async def date_point_keyboard(points: dict, current_page: int) -> InlineKeyboardMarkup:
    check_lists = points.get('check_lists', [])

    total_pages = math.ceil(len(check_lists) / 6)

    start_index = current_page * 6
    end_index = start_index + 6
    end_index = min(end_index, len(check_lists))

    page_items = check_lists[start_index:end_index]

    buttons = []
    for point_check_list in page_items:
        date_str = datetime.strptime(point_check_list['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%d.%m.%Y')
        buttons.append([InlineKeyboardButton(text=date_str, callback_data=f'point-{point_check_list["id"]}')])

    prev_callback_data = f'point-prev_page_{current_page - 1}' if current_page > 0 else '#'
    next_callback_data = f'point-next_page_{current_page + 1}' if current_page < total_pages - 1 else '#'

    navigation_buttons = [
        InlineKeyboardButton(text='⬅️', callback_data=prev_callback_data),
        InlineKeyboardButton(text=f'{current_page + 1}/{total_pages}', callback_data='#'),
        InlineKeyboardButton(text='➡️', callback_data=next_callback_data)
    ]

    buttons.append(navigation_buttons)

    buttons.append([InlineKeyboardButton(text='Назад', callback_data='check_list_point')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard