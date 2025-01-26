from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot import keyboards
from bot.states import ChangeEmployeeState
from bot.services import users_service

callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'change_employee')
async def change_employee(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    await state.set_state(ChangeEmployeeState.tg_id)
    message = await callback.message.answer_photo(
        photo=types.FSInputFile('./files/ID.png'),
        reply_markup=keyboards.functionals.change_employee.TO_BACK_KEYBOARD
    )
    await state.update_data(last_message_id=message.message_id)


@callbacks_router.callback_query(F.data.startswith('change_employee-'))
async def change_employee(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()

    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    await state.set_state(ChangeEmployeeState.tg_id)
    user = await users_service.get_by_tg_id(int(data['tg_id']))
    role = int(callback.data.split('-')[1])
    print(role)
    await users_service.update({'role': role}, int(data['tg_id']))

    message = await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Роль изменена.png'),
        reply_markup=keyboards.functionals.change_employee.TO_MAIN_MENU_KEYBOARD
    )
    await state.update_data(last_message_id=message.message_id)
