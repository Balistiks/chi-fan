import re

from aiogram import Router, types, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot.states import CashReportState
from bot import keyboards

messages_router = Router()


@messages_router.message(CashReportState.morning_recount)
async def get_morning_recount(message: types.Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=data['last_message_id'])

    if message.photo:
        await message.answer(
            text='Кассовый отчет',
            reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(0)
        )
    elif message.document:
        await message.answer(
            text='Кассовый отчет',
            reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(0)
        )
    else:
        await state.set_state(CashReportState.morning_recount)
        message = await message.answer(
            text=f'Прикрепите {data['type']}'
        )
        await state.update_data(last_message_id=message.message_id)


@messages_router.message(CashReportState.money_begin)
async def get_money_begin(message: types.Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.delete_message(chat_id=message.chat.id, message_id=data['last_message_id'])
    if message.text.isdigit():
        await message.answer(
            text='Кассовый отчет',
            reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(0)
        )
    else:
        await state.set_state(CashReportState.money_begin)
        message = await message.answer(
            text='Введите сумму'
        )
        await state.update_data(last_message_id=message.message_id)


@messages_router.message(CashReportState.collected_fullname)
async def get_money_begin(message: types.Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.delete_message(chat_id=message.chat.id, message_id=data['last_message_id'])

    full_name = message.text
    name_pattern = re.compile(r'^[а-яёА-ЯЁ]+ [а-яёА-ЯЁ]+ [а-яёА-ЯЁ]+$', re.IGNORECASE)

    if name_pattern.match(full_name):
        await message.answer(
            text='Кассовый отчет',
            reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(0)
        )
    else:
        await state.set_state(CashReportState.collected_fullname)
        message = await message.answer(
            text='Введите ФИО'
        )
        await state.update_data(last_message_id=message.message_id)