from datetime import datetime, timedelta

from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot.services import points_service
from bot.states import CashReportState
from bot import keyboards


callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'cash_report')
async def cash_report(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    date_today = datetime.now().strftime('%d.%m.%Y')
    date_yesterday = (datetime.now() - timedelta(days=1)).strftime('%d.%m.%Y')

    await callback.message.answer(
        text='Выберите день',
        reply_markup=await keyboards.functionals.cash_report.date_keyboard(date_today, date_yesterday)
    )


@callbacks_router.callback_query(F.data.startswith('date:'))
async def date(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(date=callback.data.split(':')[1])

    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    points_names = await points_service.get_names()

    await callback.message.answer(
        text='Выберите точку',
        reply_markup=await keyboards.functionals.cash_report.points_keyboard(points_names)
    )


@callbacks_router.callback_query(F.data.startswith('cash_point:'))
async def cash_point(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    await state.update_data(point_name=callback.data.split(':')[1])

    await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Кассовый отчет главная.png'),
        reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(0)
    )


@callbacks_router.callback_query(F.data.startswith('cash_report-prev_page'))
@callbacks_router.callback_query(F.data.startswith('cash_report-next_page'))
async def slider_cash_report(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current_page = data.get('current_page', 0)

    if 'prev_page' in callback.data:
        current_page -= 1
    elif 'next_page' in callback.data:
        current_page += 1

    await state.update_data(current_page=current_page)

    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text='Кассовый отчет',
        reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(current_page)
    )


@callbacks_router.callback_query(F.data.startswith('recount:'))
async def recount(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await state.set_state(CashReportState.recount)
    message = await callback.message.answer(
        text='Прикрепите видео'
    )
    await state.update_data(last_message_id=message.message_id, recount_data=callback.data.split(':')[1])


@callbacks_router.callback_query(F.data.startswith('checks_file:'))
async def checks_file(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await state.set_state(CashReportState.checks_file)
    message = await callback.message.answer(
        text='Прикрепите файл'
    )
    await state.update_data(last_message_id=message.message_id, recount_data=callback.data.split(':')[1])


@callbacks_router.callback_query(F.data.startswith('enter_sum:'))
async def enter_sum(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await state.set_state(CashReportState.enter_sum)
    data_callback = callback.data.split(':')[1]
    message = await callback.message.answer(
        text='Введите сумму'
    )
    await state.update_data(last_message_id=message.message_id, data_cash=data_callback)


@callbacks_router.callback_query(F.data == 'collected_fullname')
async def collected_fullname(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await state.set_state(CashReportState.collected_fullname)
    message = await callback.message.answer(
        text='Введите ФИО'
    )
    await state.update_data(last_message_id=message.message_id)
