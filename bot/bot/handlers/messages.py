from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.filters import IsExistFilter
from bot import keyboards

messages_router = Router()


@messages_router.message(CommandStart(), IsExistFilter(),)
async def start_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text='Привет! Мы рады приветствовать тебя в команде <b>Чи-Фань</b> 🎉\n\n'
             'Здесь ты найдешь всю важную информацию для комфортной и продуктивной работы:\n\n'
             '💰 <b>Зарплата</b>\n🕒 <b>График смен</b>\n📋 <b>Инструкции и регламенты</b>\n\n'
             'Спасибо, что стал частью нашей команды! Мы ценим твою энергию и вклад. Вместе у нас всё получится! 🚀',
        parse_mode='HTML',
        reply_markup=await keyboards.main_menu(message.from_user.id)
    )
