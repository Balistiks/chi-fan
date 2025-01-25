import re

from aiogram import Router, types, Bot
from aiogram.fsm.context import FSMContext

from bot import keyboards
from bot.states import NewEmployeeState
from bot.services import users_service, names_service
from bot.misc import functions

messages_router = Router()


@messages_router.message(NewEmployeeState.tg_id)
async def get_tg_id(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()

    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=data['last_message_id'])
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)

    await state.update_data(tg_id=message.text)
    await state.set_state(NewEmployeeState.name)

    message = await message.answer_photo(
        photo=types.FSInputFile('./files/ФИО.png'),
        reply_markup=await keyboards.functionals.new_employee.to_back_tg_id_keyboard(data['role_id'])
    )
    await state.update_data(last_message_id=message.message_id)


@messages_router.message(NewEmployeeState.name)
async def get_name(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()

    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=data['last_message_id'])
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)

    name_pattern = re.compile(r"^[А-ЯЁË][а-яёë]*\s[А-ЯЁË][а-яёë]*$", re.IGNORECASE)

    is_exist = await names_service.is_exist(message.text)

    if re.match(name_pattern, message.text) and is_exist:
        await state.update_data(name=message.text)

        await users_service.save({
            "tgId": data['tg_id'],
            "name": message.text,
            "role": data['role_id'],
        })

        await message.answer_photo(
            photo=types.FSInputFile('./files/Пользователь добавлен.png'),
            reply_markup=keyboards.functionals.new_employee.TO_MAIN_MENU_KEYBOARD
        )
    else:
        await message.answer_photo(
            photo=types.FSInputFile('./files/Не получилось пользователь.png'),
            reply_markup=keyboards.functionals.new_employee.REPLAY_KEYBOARD
        )
