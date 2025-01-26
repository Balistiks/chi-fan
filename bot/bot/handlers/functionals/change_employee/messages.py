import re

from aiogram import Router, types, Bot
from aiogram.fsm.context import FSMContext

from bot import keyboards
from bot.states import ChangeEmployeeState
from bot.services import users_service, names_service
from bot.misc import functions

messages_router = Router()


@messages_router.message(ChangeEmployeeState.tg_id)
async def get_tg_id(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()

    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=data['last_message_id'])
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)

    user = await users_service.get_by_tg_id(int(message.text))
    await state.update_data(tg_id=message.text, name=user['name'])

    await message.answer_photo(
        photo=types.FSInputFile('./files/Выберите роль.png'),
        caption=f'Пользователь:\n\n- {user['name']}\n- {user['role']['name']}\n\nВыберите новую роль',
        reply_markup=keyboards.functionals.change_employee.ROLES_KEYBOARD
    )