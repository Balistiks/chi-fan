from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot import keyboards
from bot.states import NewEmployeeState

callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'new_employee')
async def new_employee(callback: types.CallbackQuery, bot: Bot, state: FSMContext):

    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    await callback.message.answer(
        text='Выберите роль',
        reply_markup=keyboards.functionals.new_employee.ROLES_KEYBOARD
    )


@callbacks_router.callback_query(F.data.startswith('employee-'))
async def employee(callback: types.CallbackQuery, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    await state.update_data(role_id=callback.data.split('-')[1])
    await state.set_state(NewEmployeeState.tg_id)
    message = await callback.message.answer(
        text='Введите ID пользователя\n\nДля получения пользователю нужно зайти в бота - @getmyid_bot и написать /start',
        reply_markup=keyboards.functionals.new_employee.TO_ROLES_BACK_KEYBOARD
    )
    await state.update_data(last_message_id=message.message_id)
