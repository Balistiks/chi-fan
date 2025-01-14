import math

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


data_cash_report_keyboard = [
    {
        'name': 'Утренний пересчет 📷',
        'callback': 'morning_recount'
    },
    {
        'name': 'Денег на начало дня',
        'callback': 'money_begin'
    },
    {
        'name': 'Приход',
        'callback': 'coming'
    },
    {
        'name': 'Инкассация (сумма)',
        'callback': 'collection_amount'
    },
    {
        'name': 'Инкассировал (ФИО)',
        'callback': 'collected_fullname'
    },
    {
        'name': 'Сверка итогов',
        'callback': 'reconciliation_results'
    },
    {
        'name': 'Сверка итогов по QR',
        'callback': 'reconciliation_results_QR'
    },
    {
        'name': 'Сумма доставки Яндекс',
        'callback': 'yandex_delivery_sum'
    },
    {
        'name': 'Итого чек',
        'callback': 'total_check'
    },
    {
        'name': 'Количество заказов',
        'callback': 'number_orders'
    },
    {
        'name': 'Денег на конец дня (факт)',
        'callback': 'money_end_day'
    },
    {
        'name': 'Вечерний пересчет 📷',
        'callback': 'evening_recount'
    },
    {
        'name': 'Заказы с приложения (online)',
        'callback': 'orders_application'
    },
    {
        'name': 'Бонусы с приложения',
        'callback': 'bonuses_application'
    },
    {
        'name': 'Чеки (pdf файл)',
        'callback': 'checks_pdf'
    },
    {
        'name': 'Чеки расходов 📷',
        'callback': 'expense_receipts'
    },
]

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


CHOOSE_FORMAT_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Прикрепите фото', callback_data='attach_photo'),
        ],
        [
            InlineKeyboardButton(text='Прикрепите файл', callback_data='attach_file'),
        ],
    ]
)