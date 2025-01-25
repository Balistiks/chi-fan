from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def swap_keyboard(main_tg_id: int, swap_tg_id: int) -> InlineKeyboardMarkup:
    buttons = []

    buttons.append([InlineKeyboardButton(text='Принять', callback_data=f'swap:{main_tg_id}:{swap_tg_id}')])
    buttons.append([InlineKeyboardButton(text='Отклонить', callback_data=f'swapno:{main_tg_id}')])

    return (InlineKeyboardMarkup(inline_keyboard=buttons))