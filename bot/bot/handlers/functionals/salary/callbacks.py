from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext

from bot.misc import functions

from bot import keyboards

# TEST
from bot.misc import test

callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'salary')
async def salary(callback: types.CallbackQuery, bot: Bot):
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer(
        text='Выбери месяц, чтобы узнать подробности 📅\n\n'
             'После этого ты сможешь детально изучить информацию о своей зарплате 💰',
        reply_markup=keyboards.functionals.salary.SALARY_MOUNTHS_KEYBOARD
    )


@callbacks_router.callback_query(F.data.startswith('salary_'))
async def salary_detailing(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    mounth = callback.data.split('_')[1]
    await state.update_data(mounth=mounth)

    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer(
        text='Зарплата — это всегда приятный момент! А у нас всё чётко и вовремя:\n\n'
             '<b>- За первую половину месяца (1–15 числа)</b> — деньги на карте уже <b>20 числа</>.\n'
             '<b>- За вторую половину (16–30/31 числа)</b> — ждите пополнения <b>5 числа</b>.\n\n'
             'Планируйте свои траты, а о выплатах мы позаботимся 💼',
        parse_mode='HTML',
        reply_markup=keyboards.functionals.salary.DETAILING_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'detailing_by_points')
async def salary_by_points(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    mounth = data['mounth']
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer(
        text='Детализация по точкам',
        reply_markup=await keyboards.functionals.salary.salary_points_keyboard(test, mounth)
    )


@callbacks_router.callback_query(F.data.startswith('salary-point_'))
async def salary_point(callback: types.CallbackQuery, bot: Bot):
    id = callback.data.split('_')[1]
    for test_item in test:
        if test_item['id'] == int(id):
            data = test_item
            break
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer_photo(
        photo=types.FSInputFile('./files/chatademia.png'),
        caption='<b>Итоги по вашим выплатам на этой точке:</b> \n\n'
                f'<b>С 1 по 15 число</b> вы заработали:\n👉 {data['salary']}\n'
                f'<b>С 16 по 30/31 число</b> на вашем счету оказалось:\n👉 {data['salary']}\n\n'
                'Ваш труд ценен, а заработанное — заслуженно ваше! 🚀🔥',
        parse_mode='HTML',
        reply_markup=keyboards.functionals.salary.BACK_DETAILING_KEYBOARD
    )


@callbacks_router.callback_query(F.data == 'detailing_by_days')
async def salary_by_days(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    mounth = data['mounth']
    await functions.delete_message(bot=bot, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    analytics_text = "<b>Детальная аналитика по дням за месяц</b> 📅\n\n"
    analytics_text += "<b>- Дата | Точка | Сумма </b>\n"

    for item in test:
        if item['month'] == mounth:
            for date, salary in item['daily_salary'].items():
                analytics_text += f"{date} | {item['name']:<11} | {salary:<5}\n"

    await callback.message.answer(
        text=analytics_text,
        parse_mode='HTML',
        reply_markup=keyboards.functionals.salary.BACK_DETAILING_BY_DAYS_KEYBOARD
    )

