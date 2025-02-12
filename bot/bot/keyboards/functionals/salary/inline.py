from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_salary_months_keyboard(months: dict) -> InlineKeyboardMarkup:
    buttons = []

    salary_per_month = {}
    for key, value in months.items():
        salary_per_month[key] = 0
        for salary in months[key]:
            salary_per_month[key] += salary['sum']

    for i in range(len(salary_per_month)):
        month = list(salary_per_month.keys())[i]
        salary = f'{salary_per_month[month]:,}'.replace(',', ' ')
        buttons.append([InlineKeyboardButton(text=f'{month} - {salary}₽', callback_data=f'salary_{i+1}')])

    buttons.append([InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


SALARY_MOUNTHS_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Январь', callback_data='salary_1'),
        ],
        [
            InlineKeyboardButton(text='Февраль', callback_data='salary_2'),
        ],
        [
            InlineKeyboardButton(text='Март', callback_data='salary_3'),
        ],
        [
            InlineKeyboardButton(text='Апрель', callback_data='salary_4'),
        ],
        [
            InlineKeyboardButton(text='Май', callback_data='salary_5'),
        ],
        [
            InlineKeyboardButton(text='Июнь', callback_data='salary_6'),
        ],
        [
            InlineKeyboardButton(text='Июль', callback_data='salary_7'),
        ],
        [
            InlineKeyboardButton(text='Август', callback_data='salary_8'),
        ],
        [
            InlineKeyboardButton(text='Сентябрь', callback_data='salary_9'),
        ],
        [
            InlineKeyboardButton(text='Октябрь', callback_data='salary_10'),
        ],
        [
            InlineKeyboardButton(text='Ноябрь', callback_data='salary_11'),
        ],
        [
            InlineKeyboardButton(text='Декабрь', callback_data='salary_12'),
        ],
        [
            InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu'),
        ],
    ]
)

DETAILING_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Детализация по точкам', callback_data='detailing_by_points'),
        ],
        [
            InlineKeyboardButton(text='Детализация по дням', callback_data='detailing_by_days'),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='salary'),
        ],
    ]
)

BACK_DETAILING_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='detailing_by_points'),
        ],
    ]
)

async def back_by_days_keyboard(month: str) -> InlineKeyboardMarkup:
    buttons = []

    buttons.append([InlineKeyboardButton(text='Назад', callback_data=f'salary_{month}')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def salary_points_keyboard(points: list, month: str) -> InlineKeyboardMarkup:
    buttons = []

    for point in points:
        button = InlineKeyboardButton(text=point, callback_data=f'salary-point_{point}')
        buttons.append([button])

    buttons.append([InlineKeyboardButton(text='Назад', callback_data=f'salary_{month}')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard