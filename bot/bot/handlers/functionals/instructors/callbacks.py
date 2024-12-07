from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot import keyboards
from bot.services import topics_service, headers

callbacks_router = Router()


def get_page(callback_data, current_page):
    if callback_data == 'prev_page':
        return current_page - 1
    elif callback_data == 'next_page':
        return current_page + 1
    return current_page


@callbacks_router.callback_query(F.data == 'instructors')
async def instructors(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    media_group_ids = data.get('media_group_ids', [])

    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    if media_group_ids:
        for media_group_id in media_group_ids:
            await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=media_group_id)
        await state.clear()

    await callback.message.answer(
        text='Здесь вы найдете инструкции для работы 📚\n\n'
             'Вы можете просмотреть их в виде удобного набора картинок или открыть полный файл для более детального изучения.\n\n'
             'Приятной работы 😊',
        reply_markup=await keyboards.functionals.instructors.instructor_keyboard()
    )


@callbacks_router.callback_query(F.data.in_({'prev_page', 'next_page'}))
@callbacks_router.callback_query(F.data.startswith('topic_'))
async def topic(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    media_group_ids = data.get('media_group_ids', [])
    current_page = data.get('current_page', 1)

    callback_data = callback.data
    topic_id = callback_data.split('_')[1]
    topic_data = await topics_service.get_by_id(topic_id)

    if topic_id == 'page':
        current_page = get_page(callback_data, current_page)
        await state.update_data(current_page=current_page)

    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    if media_group_ids:
        for media_group_id in media_group_ids:
            await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=media_group_id)
        await state.clear()

    if not topic_data['subTopics']:
        if topic_data['photos'] != []:
            media_group = []
            path_photos = topic_data['photos']

            for photo in path_photos:
                media = types.InputMediaPhoto(
                    media=types.URLInputFile(
                        headers=headers,
                        url=f"http://back:3000/api/photos/{photo['path']}",
                        filename=photo['path']
                    )
                )
                media_group.append(media)
            media_group = await callback.message.bot.send_media_group(
                chat_id=callback.message.chat.id,
                media=media_group
            )
            media = []
            for media_id in media_group:
                media_id = media_id.message_id
                media.append(media_id)
            await state.update_data(media_group_ids=media)
        await callback.message.answer(
            text=f'{topic_data['text']}',
            reply_markup=await keyboards.functionals.instructors.instructor_topic_menu_keyboard(topic_id, current_page)
        )
    elif topic_data['subTopics']:
        await callback.message.answer(
            text='Инструкции',
            reply_markup=await keyboards.functionals.instructors.instructor_topic_keyboard(topic_id)

        )


@callbacks_router.callback_query(F.data.startswith('topic-file_'))
async def topic_file(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    media_group_ids = data.get('media_group_ids', [])

    callback_data = callback.data
    path_file = callback_data.split('_')[1]
    topic_id = callback_data.split('_')[2]

    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    if media_group_ids:
        for media_group_id in media_group_ids:
            await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=media_group_id)
        await state.clear()

    await callback.message.answer_document(
        document=types.URLInputFile(
            headers=headers,
            url=f"http://back:3000/api/files/{path_file}",
            filename=path_file
        ),
        reply_markup=await keyboards.functionals.instructors.instructor_topic_back_keyboard(topic_id)
    )

