from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


SALARY_MOUNTHS_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Январь', callback_data='salary_Январь'),
        ],
        [
            InlineKeyboardButton(text='Февраль', callback_data='salary_Февраль'),
        ],
        [
            InlineKeyboardButton(text='Март', callback_data='salary_Март'),
        ],
        [
            InlineKeyboardButton(text='Апрель', callback_data='salary_Апрель'),
        ],
        [
            InlineKeyboardButton(text='Май', callback_data='salary_Май'),
        ],
        [
            InlineKeyboardButton(text='Июнь', callback_data='salary_Июнь'),
        ],
        [
            InlineKeyboardButton(text='Июль', callback_data='salary_Июль'),
        ],
        [
            InlineKeyboardButton(text='Август', callback_data='salary_Август'),
        ],
        [
            InlineKeyboardButton(text='Сентябрь', callback_data='salary_Сентябрь'),
        ],
        [
            InlineKeyboardButton(text='Октябрь', callback_data='salary_Октябрь'),
        ],
        [
            InlineKeyboardButton(text='Ноябрь', callback_data='salary_Ноябрь'),
        ],
        [
            InlineKeyboardButton(text='Декабрь', callback_data='salary_Декабрь'),
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

BACK_DETAILING_BY_DAYS_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='salary_'),
        ],
    ]
)


async def salary_points_keyboard(points: list, mounth: str) -> InlineKeyboardMarkup:
    buttons = []

    for point in points:
        button = InlineKeyboardButton(text=point['name'], callback_data=f'salary-point_{point['id']}')
        buttons.append([button])

    buttons.append([InlineKeyboardButton(text='Назад', callback_data=f'salary_{mounth}')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard