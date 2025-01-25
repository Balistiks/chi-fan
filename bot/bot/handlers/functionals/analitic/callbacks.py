from collections import defaultdict
from datetime import datetime, timedelta

from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot import keyboards
from bot.services import revenues_service

callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'analitic')
async def analitic(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    await callback.message.answer(
        text='Выручка',
        reply_markup=keyboards.functionals.analitic.CHOOSE_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'all_point')
async def all_point(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    data_revenues = await revenues_service.get_all()

    revenues_by_point = defaultdict(int)
    for revenue in data_revenues:
        point_name = revenue['point']['name']
        revenues_by_point[point_name] += revenue['amount']

    message_text = 'Детальная аналитика за месяц  📅\n\n- Точка | Выручка | Процент от плана\n\n'

    total_revenue = 0
    for point, amount in revenues_by_point.items():
        message_text += f'- {point} | {amount} | \n'
        total_revenue += amount

    message_text += f'\nОбщий факт:\nОбщий план:\nПроцент от плана:'
    await callback.message.answer(
        text=message_text,
        reply_markup=keyboards.functionals.analitic.TO_BACK_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'by_point')
async def by_point(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    data_revenues = await revenues_service.get_all()

    await callback.message.answer(
        text='Выберите точку',
        reply_markup=await keyboards.functionals.analitic.get_point_keyboard(data_revenues=data_revenues)
    )


@callbacks_router.callback_query(F.data.startswith('analitic:'))
async def get_analitic(callback: types.CallbackQuery, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    await state.update_data(point_id=callback.data.split(':')[1])

    message = await callback.message.answer(
        text='Выберите период',
        reply_markup=keyboards.functionals.analitic.DATES_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'day')
async def day(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    data = await state.get_data()

    await callback.message.answer(
        text='Выручка',
        reply_markup=await keyboards.functionals.analitic.get_day_point_keyboard(point_id=data['point_id'])
    )


@callbacks_router.callback_query(F.data.startswith('day:'))
async def get_day(callback: types.CallbackQuery, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    data_revenues = await revenues_service.get_by_id_amount(callback.data.split(':')[1])
    date = datetime.strptime(data_revenues['date'], "%Y-%m-%d").strftime("%d.%m.%Y")

    await callback.message.answer(
        text=f'Детальная аналитика по дням за месяц  📅\n\n'
              f'- Дата | Точка | Выручка\n{date} | {data_revenues["point"]['name']} | {data_revenues['amount']}\n\n'
              'Процент от плана: ',
        reply_markup=keyboards.functionals.analitic.TO_BACK_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'week')
async def week(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    data = await state.get_data()

    await callback.message.answer(
        text='Выручка',
        reply_markup=await keyboards.functionals.analitic.get_week_point_keyboard(point_id=data['point_id'])
    )


@callbacks_router.callback_query(F.data.startswith('week:'))
async def get_week(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    data = await state.get_data()

    week_index = int(callback.data.split(':')[1])
    data_revenues = await revenues_service.get_by_id(data['point_id'])


    dates = sorted(list({datetime.strptime(revenue['date'], "%Y-%m-%d").date() for revenue in data_revenues}))

    min_date = dates[0]
    max_date = dates[-1]

    periods = [
          (min_date + timedelta(days=i*7), min(max_date, min_date + timedelta(days=i*7 + 6)))
          for i in range((max_date - min_date).days // 7 + 1)
    ]
    start_date, end_date = periods[week_index]

    message_text = f'Детальная аналитика по дням за период 📅\n\n' \
                   f'- Дата | Точка | Выручка\n'

    total_revenue = 0
    for revenue in data_revenues:
        date = datetime.strptime(revenue['date'], "%Y-%m-%d").date()
        if start_date <= date <= end_date:
            formatted_date = date.strftime("%d.%m.%Y")
            message_text += f'{formatted_date} | {revenue["point"]["name"]} | {revenue["amount"]}\n'
            total_revenue += revenue['amount']

    message_text += f'Процент от плана: '

    await callback.message.answer(
        text=message_text,
        reply_markup=keyboards.functionals.analitic.TO_BACK_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'month')
async def month(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    data = await state.get_data()
    point_id = data.get('point_id')

    data_revenues = await revenues_service.get_by_id(point_id)

    if not data_revenues:
       await callback.message.answer("Нет данных о выручке за этот месяц.")
       return


    message_text = 'Детальная аналитика по дням за месяц  📅\n\n- Дата | Точка | Выручка\n\n'
    total_revenue = 0

    for record in data_revenues:
        date_str = datetime.fromisoformat(record['date']).strftime("%Y-%m-%d")
        point_name = record['point']['name']
        revenue = record['amount']
        message_text += f"- {date_str} | {point_name} | {revenue}\n"
        total_revenue += revenue


    message_text += f"\nПроцент от плана: "


    await callback.message.answer(
        text=message_text,
        reply_markup=keyboards.functionals.analitic.TO_BACK_KEYBOARD
    )
