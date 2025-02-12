from datetime import datetime

from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions
from bot.services import salaries_service, users_service
from bot import keyboards

# TEST
from bot.misc import test

callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'salary')
async def salary(callback: types.CallbackQuery, bot: Bot):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    user = await users_service.get_by_tg_id(callback.from_user.id)
    months = await salaries_service.get_months(user['name'])
    await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Зарплаты.png'),
        caption='Выбери месяц, чтобы узнать подробности 📅\n\n'
             'После этого ты сможешь детально изучить информацию о своей зарплате 💰',
        reply_markup=keyboards.functionals.salary.get_salary_months_keyboard(months)
    )


@callbacks_router.callback_query(F.data.startswith('salary_'))
async def salary_detailing(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    mouth = callback.data.split('_')[1]
    await state.update_data(mouth=mouth)

    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Детализация зарплат.png'),
        caption='Зарплата — это всегда приятный момент! А у нас всё чётко и вовремя:\n\n'
             '<b>- За первую половину месяца (1–15 числа)</b> — деньги на карте уже <b>20 числа</>.\n'
             '<b>- За вторую половину (16–30/31 числа)</b> — ждите пополнения <b>5 числа</b>.\n\n'
             'Планируйте свои траты, а о выплатах мы позаботимся 💼',
        parse_mode='HTML',
        reply_markup=keyboards.functionals.salary.DETAILING_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'detailing_by_points')
async def salary_by_points(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    user = await users_service.get_by_tg_id(callback.from_user.id)
    user_name = user['name']
    mouth = data['mouth']
    points = await salaries_service.get_names_points(user_name, mouth)
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    await state.update_data(mouth=mouth, user_name=user_name)
    await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Детализация по точкам.png'),
        reply_markup=await keyboards.functionals.salary.salary_points_keyboard(points, mouth)
    )


@callbacks_router.callback_query(F.data.startswith('salary-point_'))
async def salary_point(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    point_name = callback.data.split('_')[1]
    sums = await salaries_service.get_sums(point_name, data['user_name'], data['mouth'])
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer(
        text='<b>Итоги по вашим выплатам на этой точке:</b> \n\n'
                f'<b>С 1 по 15 число</b> вы заработали:\n👉 {sums['sum1']}\n'
                f'<b>С 16 по 30/31 число</b> на вашем счету оказалось:\n👉 {sums['sum2']}\n\n'
                'Ваш труд ценен, а заработанное — заслуженно ваше! 🚀🔥',
        parse_mode='HTML',
        reply_markup=keyboards.functionals.salary.BACK_DETAILING_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'detailing_by_days')
async def salary_by_days(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    user = await users_service.get_by_tg_id(callback.from_user.id)
    user_name = user['name']
    mouth = data['mouth']
    data_salary = await salaries_service.get_by_name_point_employee_name(user_name, mouth)
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    analytics_text = "<b>Детальная аналитика по дням за месяц</b> 📅\n\n"
    analytics_text += "<b>- Дата | Точка | Сумма </b>\n"


    for item in data_salary:
        date_str = datetime.strptime(item['date'], '%Y-%m-%d').strftime('%d.%m.%Y')
        analytics_text += f"- {date_str} | {item['pointName']} | {item['sum']}\n"

    await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Детализация по дням.png'),
        caption=analytics_text,
        parse_mode='HTML',
        reply_markup=await keyboards.functionals.salary.back_by_days_keyboard(mouth)
    )


