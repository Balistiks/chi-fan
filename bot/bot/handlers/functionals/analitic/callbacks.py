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
    date = datetime.today()- timedelta(days=1)
    await state.update_data(yestarday_date=date.strftime("%Y-%m-%d"))
    await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Выручка.png'),
        reply_markup=await keyboards.functionals.analitic.choose_point(date=date.strftime('%d.%m.%Y'))
    )


@callbacks_router.callback_query(F.data == 'all_point')
async def all_point(callback: types.CallbackQuery, bot: Bot, state: FSMContext, sheet):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    data_revenues = await revenues_service.get_all()

    result = sheet.values().get(
        spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
        range='Аналитика!K2'
    ).execute()

    value_str = result.get('values', [[]])[0][0]
    cent_plan = value_str.replace(' ', '').replace('\xa0', '').replace('₽', '').strip()
    plan_amount = int(cent_plan)

    total_sum = 0
    revenues_by_point = defaultdict(int)

    for revenue in data_revenues:
        point_name = revenue['point']['name']
        revenues_by_point[point_name] += revenue['amount']
        total_sum += revenue['amount']

    message_text = 'Детальная аналитика за месяц 📅\n\n'
    message_text += '<pre>Точка        | Выручка      | Процент от плана\n'

    for point, amount in revenues_by_point.items():
        formatted_amount = "{:,.0f}".format(amount).replace(',', ' ') + "₽"
        percentage_of_plan = (amount / plan_amount) * 100
        message_text += f'{point:<12} | {formatted_amount:<12} | {percentage_of_plan:.2f}%\n'
    message_text += "</pre>"
    percent_of_plan = (total_sum / plan_amount) * 100
    formatted_total_sum = "{:,.0f}".format(total_sum).replace(',', ' ')
    formatted_plan_amount = "{:,.0f}".format(plan_amount).replace(',', ' ')

    message_text += f'\nОбщий факт: {formatted_total_sum}₽\n'
    message_text += f'Общий план: {formatted_plan_amount}₽\n'
    message_text += f'Процент от плана: {percent_of_plan:.2f}%'
    await callback.message.answer(
        text=message_text,
        parse_mode='HTML',
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


@callbacks_router.callback_query(F.data == 'yestarday_analitic')
async def analiyestarday_analitictic(callback: types.CallbackQuery, bot: Bot, state: FSMContext, sheet):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    data = await state.get_data()
    revenues = await revenues_service.get_by_date(data['yestarday_date'])

    total_sum = 0
    revenues_by_point = defaultdict(int)

    result = sheet.values().get(
        spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
        range='Аналитика!K2'
    ).execute()

    value_str = result.get('values', [[]])[0][0]
    cent_plan = value_str.replace(' ', '').replace('\xa0', '').replace('₽', '').strip()
    plan_amount = int(cent_plan)

    for revenue in revenues:
        point_name = revenue['point']['name']
        revenues_by_point[point_name] += revenue['amount']
        total_sum += revenue['amount']

    message_text = 'Детальная аналитика за вчера 📅\n\n'
    message_text += '<pre>Точка        | Выручка      | Процент от плана\n'

    for point, amount in revenues_by_point.items():
        formatted_amount = "{:,.0f}".format(amount).replace(',', ' ') + "₽"
        percentage_of_plan = (amount / plan_amount) * 100 if plan_amount > 0 else 0
        message_text += f'{point:<12} | {formatted_amount:<12} | {percentage_of_plan:.2f}%\n'

    message_text += "</pre>"
    formatted_total_sum = "{:,.0f}".format(total_sum).replace(',', ' ')
    formatted_plan_amount = "{:,.0f}".format(plan_amount).replace(',', ' ')

    message_text += f'\nОбщий факт: {formatted_total_sum}₽\nОбщий план: {formatted_plan_amount}₽'

    await callback.message.answer(
        text=message_text,
        parse_mode='HTML',
        reply_markup=keyboards.functionals.analitic.TO_BACK_KEYBOARD
    )



@callbacks_router.callback_query(F.data.startswith('analitic:'))
async def get_analitic(callback: types.CallbackQuery, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    await state.update_data(point_id=callback.data.split(':')[1])

    message = await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Выбепите период.png'),
        reply_markup=keyboards.functionals.analitic.DATES_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'day')
async def day(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    data = await state.get_data()

    await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Выберите день.png'),
        reply_markup=await keyboards.functionals.analitic.get_day_point_keyboard(point_id=data['point_id'])
    )


@callbacks_router.callback_query(F.data.startswith('day:'))
async def get_day(callback: types.CallbackQuery, state: FSMContext, sheet):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    data_revenues = await revenues_service.get_by_id_amount(callback.data.split(':')[1])
    date = datetime.strptime(data_revenues['date'], "%Y-%m-%d").strftime("%d.%m.%Y")

    result = sheet.values().get(
        spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
        range='Аналитика!K2'
    ).execute()

    value_str = result.get('values', [[]])[0][0]

    cent_plan = value_str.replace(' ', '').replace('\xa0', '').replace('₽', '').strip()
    plan_amount = int(cent_plan)

    actual_revenue = data_revenues['amount']
    percent_of_plan = (actual_revenue / plan_amount) * 100
    formatted_actual_revenue = "{:,}".format(int(actual_revenue)).replace(',', ' ')

    await callback.message.answer(
        text=f'Детальная аналитика по дням за месяц  📅\n\n'
              f'<pre>Дата       | Точка        | Выручка\n{date:<10} | {data_revenues["point"]['name']:<12} | {formatted_actual_revenue}₽</pre>\n\n'
              f'Процент от плана: {percent_of_plan:.2f}% ',
        parse_mode='HTML',
        reply_markup=keyboards.functionals.analitic.TO_BACK_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'week')
async def week(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    data = await state.get_data()

    await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Выручка.png'),
        reply_markup=await keyboards.functionals.analitic.get_week_point_keyboard(point_id=data['point_id'])
    )


@callbacks_router.callback_query(F.data.startswith('week:'))
async def get_week(callback: types.CallbackQuery, bot: Bot, state: FSMContext, sheet):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    data = await state.get_data()

    week_index = int(callback.data.split(':')[1])
    data_revenues = await revenues_service.get_by_id(data['point_id'])

    result = sheet.values().get(
        spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
        range='Аналитика!K2'
    ).execute()

    value_str = result.get('values', [[]])[0][0]

    cent_plan = value_str.replace(' ', '').replace('\xa0', '').replace('₽', '').strip()
    plan_amount = int(cent_plan)

    dates = sorted(list({datetime.strptime(revenue['date'], "%Y-%m-%d").date() for revenue in data_revenues}))

    min_date = dates[0]
    max_date = dates[-1]

    periods = [
        (min_date + timedelta(days=i * 7), min(max_date, min_date + timedelta(days=i * 7 + 6)))
        for i in range((max_date - min_date).days // 7 + 1)
    ]
    start_date, end_date = periods[week_index]

    message_text = f'Детальная аналитика по дням за период 📅\n\n' \
                   f'<pre>Дата       | Точка        | Выручка\n'

    total_revenue = 0
    for revenue in data_revenues:
        date = datetime.strptime(revenue['date'], "%Y-%m-%d").date()
        if start_date <= date <= end_date:
            formatted_date = date.strftime("%d.%m.%Y")
            formatted_revenue = "{:,}".format(int(revenue['amount'])).replace(',', ' ')
            message_text += f'{formatted_date:<10} | {revenue["point"]["name"]:<12} | {formatted_revenue}₽\n'
            total_revenue += revenue['amount']
    message_text += "</pre>"
    percentage_of_plan = (total_revenue / plan_amount * 100)

    message_text += f'\nПроцент от плана: {percentage_of_plan:.2f}%'

    await callback.message.answer(
        text=message_text,
        parse_mode='HTML',
        reply_markup=keyboards.functionals.analitic.TO_BACK_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'month')
async def month(callback: types.CallbackQuery, bot: Bot, state: FSMContext, sheet):
    await functions.delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
    data = await state.get_data()
    point_id = data.get('point_id')

    data_revenues = await revenues_service.get_by_id(point_id)

    result = sheet.values().get(
        spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
        range='Аналитика!K2'
    ).execute()

    value_str = result.get('values', [[]])[0][0]

    cent_plan = value_str.replace(' ', '').replace('\xa0', '').replace('₽', '').strip()
    plan_amount = int(cent_plan)

    message_text = 'Детальная аналитика по дням за месяц 📅\n\n<pre>Дата       | Точка        | Выручка\n'
    total_revenue = 0

    for record in data_revenues:
        date_str = datetime.fromisoformat(record['date']).strftime("%Y-%m-%d")
        point_name = record['point']['name']
        revenue = record['amount']
        formatted_revenue = "{:,}".format(int(revenue)).replace(',', ' ')
        message_text += f"{date_str:<10} | {point_name:<12} | {formatted_revenue}₽\n"
        total_revenue += revenue
    message_text += "</pre>"
    percentage_of_plan = (total_revenue / plan_amount * 100) if plan_amount > 0 else 0

    message_text += f"\nПроцент от плана: {percentage_of_plan:.2f}%"

    await callback.message.answer(
        text=message_text,
        parse_mode='HTML',
        reply_markup=keyboards.functionals.analitic.TO_BACK_KEYBOARD
    )
