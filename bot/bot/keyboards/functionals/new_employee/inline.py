from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ROLES_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Менеджер смены/кассир/инструктор', callback_data='employee-1'),
        ],
        [
            InlineKeyboardButton(text='Повар/уборщицы/заготовщики', callback_data='employee-2'),
        ],
        [
            InlineKeyboardButton(text='Сотрудник офиса', callback_data='employee-3'),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='main_menu'),
        ],
    ]
)

TO_MAIN_MENU_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu'),
        ],
    ]
)

REPLAY_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить пользователя', callback_data='new_employee'),
        ],
    ]
)


TO_ROLES_BACK_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='new_employee'),
        ]
    ]
)

async def to_back_tg_id_keyboard(employee_id: str) -> InlineKeyboardMarkup:
    buttons = []
    buttons.append([InlineKeyboardButton(text='Назад', callback_data=f'employee-{employee_id}')])

    return InlineKeyboardMarkup(inline_keyboard=buttons)
