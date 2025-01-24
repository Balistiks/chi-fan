from datetime import datetime, timedelta

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.services import revenues_service


CHOOSE_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='По точкам', callback_data='by_point'),
        ],
        [
            InlineKeyboardButton(text='Общая', callback_data='all_point'),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='main_menu'),
        ]
    ]
)

TO_BACK_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='analitic'),
        ]
    ]
)

DATES_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='День', callback_data='day'),
        ],
        [
            InlineKeyboardButton(text='Неделя', callback_data='week'),
        ],
        [
            InlineKeyboardButton(text='Месяц', callback_data='month'),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='by_point'),
        ],
    ]
)

async def get_point_keyboard(data_revenues: list) -> InlineKeyboardMarkup:
    unique_points = {}

    for revenue in data_revenues:
        point = revenue['point']
        unique_points[point['name']] = point['id']

    buttons = []

    for name, id in unique_points.items():
        buttons.append([InlineKeyboardButton(
            text=f'{name}',
            callback_data=f"analitic:{id}"
        )])

    buttons.append([InlineKeyboardButton(text='Назад', callback_data='analitic')])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def get_day_point_keyboard(point_id: str) -> InlineKeyboardMarkup:
    data_revenues = await revenues_service.get_by_id(point_id)

    buttons = []

    for revenue in data_revenues:
        date = datetime.strptime(revenue['date'], "%Y-%m-%d").strftime("%d.%m.%Y")
        buttons.append([InlineKeyboardButton(
            text=date,
            callback_data=f"day:{revenue['id']}"
        )])

    buttons.append([InlineKeyboardButton(text='Назад', callback_data='by_point')])

    return InlineKeyboardMarkup(inline_keyboard=buttons)



async def get_week_point_keyboard(point_id: str) -> InlineKeyboardMarkup:
    data_revenues = await revenues_service.get_by_id(point_id)

    dates = sorted(list({datetime.strptime(revenue['date'], "%Y-%m-%d").date() for revenue in data_revenues}))

    min_date = dates[0]
    max_date = dates[-1]

    periods = [
          (min_date + timedelta(days=i*7), min(max_date, min_date + timedelta(days=i*7 + 6)))
          for i in range((max_date - min_date).days // 7 + 1)
    ]

    buttons = []
    for i, (start, end) in enumerate(periods):
        buttons.append([InlineKeyboardButton(
            text=f'{i+1} неделя',
            callback_data=f"week:{i}"
        )])

    buttons.append([InlineKeyboardButton(text='Назад', callback_data='by_point')])

    return InlineKeyboardMarkup(inline_keyboard=buttons)