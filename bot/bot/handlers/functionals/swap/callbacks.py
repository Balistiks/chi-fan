from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot.services import schedules_service
from bot import keyboards

callbacks_router = Router()


@callbacks_router.callback_query(F.data.startswith('swapno:'))
async def swap_no(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    tg_id = callback.data.split(':')[1]

    await bot.send_message(
        chat_id=tg_id,
        text='Вы получили отказ',
        reply_markup=keyboards.functionals.swap.SWAP_NO_KEYBOARD,
    )


@callbacks_router.callback_query(F.data.startswith('swap:'))
async def swap_yes(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    id_main = callback.data.split(':')[1]
    id_swap = callback.data.split(':')[2]
    tg_id = callback.data.split(':')[3]


    await schedules_service.swap(id_main, id_swap)

    await bot.send_message(
        chat_id=tg_id,
        text='Изменения в список ваших смен внесены',
        reply_markup=keyboards.functionals.swap.SWAP_NO_KEYBOARD,
    )