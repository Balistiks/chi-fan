from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot.states import CheckList

from bot import keyboards

callbacks_router = Router()


@callbacks_router.callback_query(F.data.startswith('check_list-prev_page'))
@callbacks_router.callback_query(F.data.startswith('check_list-next_page'))
async def slider_check_list(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
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
        reply_markup=await keyboards.check_list.check_list_keyboard(data['check_list_shift'], current_page)
    )


@callbacks_router.callback_query(F.data.startswith('check_list_'))
async def check_list(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    index_check_list = int(callback.data.split('_')[2])

    check_list = data['check_list_shift'][index_check_list]

    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    await state.update_data(check_list_index=index_check_list)
    if '📷' in check_list:
        await state.set_state(CheckList.photo)
        message = await callback.message.answer(
            text=f'{data['check_list_shift'][index_check_list]} - прикрепите фотографию',
        )
        await state.update_data(last_message_id=message.message_id)
    else:
        await callback.message.answer(
            text=data['check_list_shift'][index_check_list],
            reply_markup=keyboards.check_list.CONFIRM_KEYBOARD
        )


@callbacks_router.callback_query(F.data == 'check_list-confirm')
async def check_list_confirm(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    check_list_index = data.get('check_list_index', 0)
    check_list_shift = data.get('check_list_shift', [])

    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    if check_list_index < len(check_list_shift):
        check_list_shift.pop(check_list_index)

    if not check_list_shift:
        await state.clear()
        return await callback.message.answer_photo(
            photo=types.FSInputFile('./files/Приветственное сообщение.png'),
            caption='Привет! Мы рады приветствовать тебя в команде <b>Чи-Фань</b> 🎉\n\n'
                    'Здесь ты найдешь всю важную информацию для комфортной и продуктивной работы:\n\n'
                    '💰 <b>Зарплата</b>\n🕒 <b>График смен</b>\n📋 <b>Инструкции и регламенты</b>\n\n'
                    'Спасибо, что стал частью нашей команды! Мы ценим твою энергию и вклад. Вместе у нас всё получится! 🚀',
            parse_mode='HTML',
            reply_markup=await keyboards.main_menu(callback.from_user.id)
        )

    new_index = min(check_list_index, len(check_list_shift) - 1)

    await state.update_data(
        check_list_index=new_index,
        check_list_shift=check_list_shift
    )

    await callback.message.answer(
        text=data['check_list_text'],
        reply_markup=await keyboards.check_list.check_list_keyboard(check_list_shift, 0)
    )


@callbacks_router.callback_query(F.data == 'check_list-add_photo')
async def check_list_add_photo(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    await state.set_state(CheckList.photo)
    message = await callback.message.answer(
        text=f'{data['check_list_shift'][data['check_list_index']]} - прикрепите фотографию',
    )
    await state.update_data(last_message_id=message.message_id)


