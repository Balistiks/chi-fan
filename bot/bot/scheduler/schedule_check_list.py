from datetime import datetime, timedelta

from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey

from bot.services import points_service, users_service, schedules_service
from bot import keyboards


list_opening_shift = [
    'Гостевая дверь открыта 📷',
    'Заявки с других точек приняты ☑️',
    'Музыка в зале включена ☑️',
    'Стоп-лист отсутствует ☑️',
    'Кассовая смена готова к работе ☑️',
    'Прилегающая территория чистая 📷',
    'Зона мойки готова к работе 📷',
    'Зона фритюра готова к работе 📷',
    'Вок станция готова к работе 📷',
    'Телефоны сданы (кроме ст. повара и менеджера) 📷',
    'Коридор убран 📷',
    'Раздевалка чистая 📷',
    'Туалет чистый 📷',
    'Заготовка чистая и готова к работе 📷',
    'Кухня чистая и готова к работе 📷',
    'Окно в зале открыто в начале дня для проветривания 📷',
    'Логотип включен 📷',
    'Холодильник кола готов к работе📷',
    'Приток включен (если нет - пропустить) 📷',
    'Улица убрана, уличный бак чистый 📷',
    'Вход для гостей убран и готов к работе 📷',
    'Лестничная площадка - чистая 📷',
    'Мусора на балконе нет 📷',
    'Дверь в цех закрыта 📷',
    'Мусора на лестничной площадке нет ( если есть напишите Ире) 📷',
    'Ножки столов и стульев чистые 📷',
    'Мусорный бак вымыт 📷',
    'Вода с бутылке есть(для кофемашины) ☑️',
    'Фото весов поварские и кассирские 📷',
    '"Тест заказ для проверки нумерации" ☑️',
    'Калитка открыта 📷',
]

list_closing_shift = [
    'Зона сборки чистая 📷',
    'Зона вок чистая 📷',
    'Зона фритюр чистая 📷',
    'Кофемашина замыта спец химией 📷',
    'Сумка для доставок и самовывозов пустая 📷',
    'Приток и вытяжка выключены 📷',
    'Зал убран, полы в зале замыты 📷',
    'Зона мойки чистая 📷',
    'Полы в помещении вымыты 📷',
    'Вытяжка замыта 📷',
    'Свет выключен 📷',
    'Стены чистые (кассовая зона) 📷',
    'Резинки холодильника кола - чистые 📷',
    'Резинки холодильных столов - чистые 📷',
    'Коридор замыт на ночь 📷',
    'Туалет замыт на ночь 📷',
    'Мусор с балкона вынесен на площадку 📷'
    'Холдеры замыты 📷',
    'Микроволновка чистая 📷',
    'Под лестницей в зале вымыто 📷',
    'Ножки столов и стульев чистые 📷',
    'Холодильники фото внутри 📷',
    'Емкости с продуктами 📷',
]

async def schedule_opening_shift(bot: Bot, apscheduler, storage):
    today = datetime.today().date()
    date_string = today.strftime('%Y-%m-%d')
    schedules = await schedules_service.get_by_date(date=date_string)


    for schedule in schedules:
        user = await users_service.get_by_name(schedule['name'])
        if user['role']['name'] == 'Менеджер':
            time = schedule['startTime']
            time_obj = datetime.strptime(time, "%H:%M:%S").time()
            datetime_obj = datetime.combine(datetime.now().date(), time_obj)
            new_time = datetime_obj - timedelta(minutes=30)
            tg_id = user['tgId']

            apscheduler.add_job(
                send_opening_shift,
                'date',
                run_date=new_time,
                kwargs={'bot': bot, 'tgId': tg_id, 'storage': storage},
                id=str(tg_id),
                replace_existing=True
            )
        else:
            continue


async def send_opening_shift(bot: Bot, tgId: int, storage):
    state = FSMContext(
        storage=storage,
        key=StorageKey(chat_id=tgId, user_id=tgId, bot_id=bot.id)
    )
    await state.update_data(check_list_shift=list_opening_shift, check_list_text='Чек-лист - открытие')

    await bot.send_message(
        chat_id=tgId,
        text='Чек-лист - открытие',
        reply_markup=await keyboards.check_list.check_list_keyboard(list_opening_shift, 0)
    )

async def schedule_closing_shift(bot: Bot, apscheduler, storage):
    today = datetime.today().date()
    date_string = today.strftime('%Y-%m-%d')
    schedules = await schedules_service.get_by_date(date=date_string)

    for schedule in schedules:
        user = await users_service.get_by_name(schedule['name'])
        if user['role']['name'] == 'Менеджер':
            time = schedule['endTime']
            time_obj = datetime.strptime(time, "%H:%M:%S").time()
            datetime_obj = datetime.combine(datetime.now().date(), time_obj)
            new_time = datetime_obj - timedelta(minutes=30)
            tg_id = user['tgId']


            apscheduler.add_job(
                send_closing_shift,
                'date',
                run_date=new_time,
                kwargs={'bot': bot, 'tgId': tg_id, 'storage': storage},
                id=tg_id,
                replace_existing=True
            )
        else:
            continue


async def send_closing_shift(bot: Bot, tgId: int, storage):
    state = FSMContext(
        storage=storage,
        key=StorageKey(chat_id=tgId, user_id=tgId, bot_id=bot.id)
    )
    await state.update_data(check_list_shift=list_closing_shift, check_list_text='Чек-лист - закрытие')

    await bot.send_message(
        chat_id=tgId,
        text='Чек-лист - закрытие',
        reply_markup=await keyboards.check_list.check_list_keyboard(list_closing_shift, 0)
    )