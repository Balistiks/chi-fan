from aiogram import Router, types, F, Bot

from bot.misc import functions
from bot import keyboards
from bot.services import topics_service, headers

callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'instructors')
async def instructors(callback: types.CallbackQuery, bot: Bot):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer(
        text='Здесь вы найдете инструкции для работы 📚\n\n'
             'Вы можете просмотреть их в виде удобного набора картинок или открыть полный файл для более детального изучения.\n\n'
             'Приятной работы 😊',
        reply_markup=await keyboards.functionals.instructors.instructor_keyboard()
    )


@callbacks_router.callback_query(F.data.startswith('topic_'))
async def topic(callback: types.CallbackQuery, bot: Bot):
    callback_data = callback.data
    topic_id = callback_data.split('_')[1]
    topic_data = await topics_service.get_by_id(topic_id)
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    if not topic_data['subTopics']:
        await callback.message.answer(
            text=f'{topic_data['text']}',
            reply_markup=keyboards.functionals.instructors.INSTRUCTOR_TOPIC_BACK_KEYBOARD
        )
    elif topic_data['subTopics'] != None:
        if topic_data['subTopics']['photos']:
            name_photos = topic_data['subTopics']['photos']
            print(name_photos)

            await callback.message.answer_photo(
                photo=types.URLInputFile(
                    headers=headers,
                    url=f'http://back:3000/api/photos/{name_photos}',
                    filename=name_photos,
                ),
                caption='Инструкции',
                reply_markup=await keyboards.functionals.instructors.instructor_topic_keyboard(topic_id)

            )
            # await callback.message.answer(
            #     text='Инструкции',
            #     reply_markup=await keyboards.functionals.instructors.instructor_topic_keyboard(topic_id)
            # )


