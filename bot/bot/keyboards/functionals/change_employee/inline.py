from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TO_BACK_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='change_employee'),
        ]
    ]
)


ROLES_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Менеджер смены/кассир/инструктор', callback_data='change_employee-1'),
        ],
        [
            InlineKeyboardButton(text='Повар/уборщицы/заготовщики', callback_data='change_employee-2'),
        ],
        [
            InlineKeyboardButton(text='Сотрудник офиса', callback_data='change_employee-3'),
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