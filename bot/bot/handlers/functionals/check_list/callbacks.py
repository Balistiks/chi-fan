from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot.services import points_service, check_lists_service, check_list_answers_service, headers

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


@callbacks_router.callback_query(F.data.startswith('point-'))
async def get_check_list(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    check_list_id = callback.data.split('-')[1]
    check_list = await check_lists_service.get_by_id(check_list_id)
    await state.update_data(check_list=check_list, check_list_id=check_list_id)
    data = await state.get_data()

    await callback.message.answer(
        text='Чек-лист - открытие',
        reply_markup=await keyboards.functionals.check_list.check_list_keyboard(check_list, 0)
    )


@callbacks_router.callback_query(F.data.startswith('point-answer-prev_page'))
@callbacks_router.callback_query(F.data.startswith('point-answer-next_page'))
async def slider_check_list_answers(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    current_page = data.get('current_page', 0)

    if 'prev_page' in callback.data:
        current_page -= 1
    elif 'next_page' in callback.data:
        current_page += 1

    await state.update_data(current_page=current_page)

    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text='Чек-лист - открытие',
        reply_markup=await keyboards.functionals.check_list.check_list_keyboard(data['check_list'], current_page)
    )


@callbacks_router.callback_query(F.data.startswith('point_answer-'))
async def get_answer(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    data = await state.get_data()

    answer_id = callback.data.split('-')[1]
    check_list = await check_list_answers_service.get_by_id(answer_id)

    if check_list['photo']:
        await callback.message.answer_photo(
            photo=types.URLInputFile(
                headers=headers,
                url=f"http://back:3000/api/photos/{check_list['photo']['id']}",
                filename=check_list['photo']['path']
            ),
            caption=check_list['text'],
            reply_markup=await keyboards.functionals.check_list.back_keyboard(data['check_list_id'])
        )
    else:
        await callback.message.answer(
            text=f'{check_list['text']} - Выполнено',
            reply_markup=await keyboards.functionals.check_list.back_keyboard(data['check_list_id'])
        )