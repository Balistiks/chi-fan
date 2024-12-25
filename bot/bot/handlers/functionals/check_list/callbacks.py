from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot.services import points_service

from bot import keyboards

callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'check_list_point')
async def check_list_of_point(callback: types.CallbackQuery, bot: Bot):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    await callback.message.answer(
        text='Выберите точку',
        reply_markup=await keyboards.functionals.check_list.points_keyboard()
    )


@callbacks_router.callback_query(F.data.startswith('check_id-'))
async def check_list_get_id(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    point_id = callback.data.split('-')[1]
    await state.update_data(point_id=point_id)

    await callback.message.answer(
        text='Выберите месяц',
        reply_markup=keyboards.functionals.check_list.MOUNTHS_KEYBOARD
    )


@callbacks_router.callback_query(F.data.startswith('check-'))
async def check_list_get_mouth(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    mouth = callback.data.split('-')[1]
    data = await state.get_data()

    points = await points_service.get_by_id_and_mouth(data['point_id'], int(mouth))
    await state.update_data(points=points)

    # await state.update_data(mouth=mouth)

    await callback.message.answer(
        text='Выберите дату',
        reply_markup=await keyboards.functionals.check_list.date_point_keyboard(points, 0)
    )


@callbacks_router.callback_query(F.data.startswith('point-prev_page'))
@callbacks_router.callback_query(F.data.startswith('point-next_page'))
async def slider_check_list(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    current_page = data.get('current_page', 0)
    points = data.get('points', [])

    if 'prev_page' in callback.data:
        current_page -= 1
    elif 'next_page' in callback.data:
        current_page += 1

    await state.update_data(current_page=current_page)

    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text='Выберите дату',
        reply_markup=await keyboards.functionals.check_list.date_point_keyboard(points, current_page)
    )