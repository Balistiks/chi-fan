from aiogram import Bot, exceptions

async def delete_message(bot: Bot, chat_id: int, message_id: int):
    try:
        print('1')
        await bot.delete_message(chat_id, message_id)
    except exceptions.TelegramBadRequest:
        try:
            print('2')
            await bot.edit_message_reply_markup(chat_id, message_id, reply_markup=None)
        except exceptions.TelegramBadRequest:
            print('3')
            pass