from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot import keyboards

callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'main_menu')
async def main_menu(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer(
        text='Привет! Мы рады приветствовать тебя в команде <b>Чи-Фань</b> 🎉\n\n'
             'Здесь ты найдешь всю важную информацию для комфортной и продуктивной работы:\n\n'
             '💰 <b>Зарплата</b>\n🕒 <b>График смен</b>\n📋 <b>Инструкции и регламенты</b>\n\n'
             'Спасибо, что стал частью нашей команды! Мы ценим твою энергию и вклад. Вместе у нас всё получится! 🚀',
        parse_mode='HTML',
        reply_markup=await keyboards.main_menu(callback.from_user.id)
    )
