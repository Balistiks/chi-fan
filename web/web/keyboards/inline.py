from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def swap_keyboard(tg_id: int, main_id: int, swap_id: int) -> InlineKeyboardMarkup:
    buttons = []

    buttons.append([InlineKeyboardButton(text='Принять', callback_data=f'swap:{main_id}:{swap_id}:{tg_id}')])
    buttons.append([InlineKeyboardButton(text='Отклонить', callback_data=f'swapno:{tg_id}')])

    return (InlineKeyboardMarkup(inline_keyboard=buttons))