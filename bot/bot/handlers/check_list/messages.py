from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot.states import CheckList
from bot import keyboards

messages_router = Router()


@messages_router.message(CheckList.photo)
async def get_check_list_photo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.bot.delete_message(chat_id=message.chat.id, message_id=data['last_message_id'])
    await functions.delete_message(message.bot, message.chat.id, message.message_id)
    if message.photo:
        largest_photo = message.photo[-1]
        await message.answer_photo(
            photo=largest_photo.file_id,
            caption='Подтвердите фотографию или прикрепите другую',
            reply_markup=keyboards.check_list.PHOTO_CONFIRM_KEYBOARD
        )
    else:
        await state.set_state(CheckList.photo)
        message = await message.answer(
            text=f'{data['check_list_shift'][data['check_list_index']]} - прикрепите фотографию',
        )
        await state.update_data(last_message_id=message.message_id)

