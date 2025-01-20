import math

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.services import users_service


data_cash_report_keyboard = [
    {
        'name': 'Утренний пересчет 📷',
        'callback': 'recount:K'
    },
    {
        'name': 'Денег на начало дня',
        'callback': 'enter_sum:C'
    },
    {
        'name': 'Приход',
        'callback': 'coming'
    },
    {
        'name': 'Инкассация (сумма)',
        'callback': 'enter_sum:E'
    },
    {
        'name': 'Инкассировал (ФИО)',
        'callback': 'collected_fullname'
    },
    {
        'name': 'Сверка итогов',
        'callback': 'enter_sum:G'
    },
    {
        'name': 'Сверка итогов по QR',
        'callback': 'enter_sum:G'
    },
    {
        'name': 'Сумма доставки Яндекс',
        'callback': 'enter_sum:J'
    },
    {
        'name': 'Итого чек',
        'callback': '#'
    },
    {
        'name': 'Количество заказов',
        'callback': '#'
    },
    {
        'name': 'Денег на конец дня',
        'callback': 'enter_sum:M'
    },
    {
        'name': 'Вечерний пересчет 📷',
        'callback': 'recount:L'
    },
    {
        'name': 'Заказы с приложения',
        'callback': 'enter_sum:H'
    },
    {
        'name': 'Бонусы с приложения',
        'callback': 'enter_sum:I'
    },
    {
        'name': 'Чеки (pdf файл) 📸',
        'callback': 'checks_file:O'
    },
    {
        'name': 'Расходы',
        'callback': 'enter_sum:Q'
    }
]

async def date_keyboard(date_day: str, date_yesterday: str) -> InlineKeyboardMarkup:
    buttons = []

    buttons.append([InlineKeyboardButton(text='Сегодня', callback_data=f'date:{date_day}')])
    buttons.append([InlineKeyboardButton(text='Вчера', callback_data=f'date:{date_yesterday}')])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def points_keyboard(points: list) -> InlineKeyboardMarkup:
    buttons = []

    for point in points:
        buttons.append([InlineKeyboardButton(text=point['name'], callback_data=f'cash_point:{point["name"]}')])

    buttons.append([InlineKeyboardButton(text="Назад", callback_data="main_menu")])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def cash_report_keyboard(current_page: int, items_per_page: int = 8) -> InlineKeyboardMarkup:
    total_pages = math.ceil(len(data_cash_report_keyboard) / items_per_page)

    buttons = []

    start_index = current_page * items_per_page
    end_index = start_index + items_per_page
    page_items = data_cash_report_keyboard[start_index:end_index]

    for item in page_items:
        buttons.append([InlineKeyboardButton(text=item['name'], callback_data=item['callback'])])

    buttons.append([InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')])

    prev_callback_data = f'cash_report-prev_page_{current_page - 1}' if current_page > 0 else '#'
    next_callback_data = f'cash_report-next_page_{current_page + 1}' if current_page < total_pages - 1 else '#'

    navigation_buttons = [
        InlineKeyboardButton(text='⬅️', callback_data=prev_callback_data),
        InlineKeyboardButton(text=f'{current_page + 1}/{total_pages}', callback_data='#'),
        InlineKeyboardButton(text='➡️', callback_data=next_callback_data),
    ]

    buttons.append(navigation_buttons)

    return InlineKeyboardMarkup(inline_keyboard=buttons)


ATTACH_VIDEO_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Прикрепить', callback_data='attach_video'),
        ]
    ]
)