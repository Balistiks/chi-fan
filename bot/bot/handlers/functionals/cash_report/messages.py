import re
from datetime import datetime

from aiogram import Router, types, Bot
from aiogram.fsm.context import FSMContext
from googleapiclient.http import MediaIoBaseUpload

from bot.misc import functions
from bot.services import users_service, cash_report_service
from bot.states import CashReportState
from bot import keyboards

messages_router = Router()


@messages_router.message(CashReportState.recount)
async def get_morning_recount(message: types.Message, bot: Bot, state: FSMContext, files, sheet):
    data = await state.get_data()
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=data['last_message_id'])

    if message.video:
        day = datetime.strptime(data['date'], '%d.%m.%Y').timetuple().tm_yday
        file = await bot.get_file(message.video.file_id)
        video = await bot.download_file(file.file_path)
        media = MediaIoBaseUpload(video, mimetype='video/mp4')
        parent = '1R45RY17a1ZllY8IR_s4HcTmdSifScCzh' \
            if data['recount_data'] == 'K' else '1biqIsDTb9cXCdmZrlmZ1hJv05QA9_Vtp'
        try:
            resp = files.create(
                body={
                    'name': f'{data["date"]}.mp4',
                    'parents': [parent]
                },
                media_body=media,
                fields='id'
            ).execute()
            sheet.values().update(
                spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
                range=f"{data['point_name']}!{data['recount_data']}{day + 1}",
                valueInputOption="USER_ENTERED",
                body={
                    'values': [[f'https://drive.google.com/file/d/{resp["id"]}']]
                }
            ).execute()
            items = keyboards.functionals.cash_report.data_cash_report_keyboard
            for item in items:
                if item['callback'] == data['callback_data']:
                    await cash_report_service.create({
                        'name': f"{item['name']}",
                        'createAt': datetime.strptime(data['date'], '%d.%m.%Y').isoformat(),
                        'point': int(data['id_point']),
                    })

            await message.answer_photo(
                photo=types.FSInputFile('./files/Кассовый отчет главная.png'),
                reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(current_page=0,
                                                                                          day=data['day'],
                                                                                          mouth=data['mouth'],
                                                                                          year=data['year'],
                                                                                          point_name=data['point_name'])
            )
        except Exception as e:
            print(e)
            await message.answer(
                'Произошла ошибка 🚫\n'
                '\nПопробуйте снова',
                reply_markup=await keyboards.functionals.cash_report.back_keyboard(data['point_name'])
            )
    else:
        await state.set_state(CashReportState.recount)
        message = await message.answer_photo(
            photo=types.FSInputFile('./files/Добавление видео.png')
        )
        await state.update_data(last_message_id=message.message_id)


@messages_router.message(CashReportState.checks_file)
async def get_checks_file(message: types.Message, bot: Bot, state: FSMContext, files, sheet):
    data = await state.get_data()
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=data['last_message_id'])

    if message.photo:
        photo = message.photo[-1]
        file = await bot.get_file(photo.file_id)
        document = await bot.download_file(file.file_path)
        media = MediaIoBaseUpload(document, mimetype='image/png')
        parent = '1XIzUDEx_RhkrfRPzfCXdkClmDEQ3aST-'
        file_name = f'{data["date"]}.png'
        try:
            resp = files.create(
                body={
                    'name': file_name,
                    'parents': [parent]
                },
                media_body=media,
                fields='id'
            ).execute()
            sheet.values().update(
                spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
                range=f"{data['point_name']}!{data['recount_data']}{datetime.strptime(data['date'], '%d.%m.%Y').timetuple().tm_yday + 1}",
                valueInputOption="USER_ENTERED",
                body={
                    'values': [[f'https://drive.google.com/file/d/{resp["id"]}']]
                }
            ).execute()
            items = keyboards.functionals.cash_report.data_cash_report_keyboard
            for item in items:
                if item['callback'] == data['callback_data']:
                    await cash_report_service.create({
                        'name': f"{item['name']}",
                        'createAt': datetime.strptime(data['date'], '%d.%m.%Y').isoformat(),
                        'point': int(data['id_point']),
                    })
            await state.update_data(current_page=0)
            await message.answer_photo(
                 photo=types.FSInputFile('./files/Кассовый отчет главная.png'),
                reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(current_page=0,
                                                                                          day=data['day'],
                                                                                          mouth=data['mouth'],
                                                                                          year=data['year'],
                                                                                          point_name=data['point_name'])
            )
        except Exception as e:
            print(e)
            await message.answer(
                'Произошла ошибка 🚫\n'
                '\nПопробуйте снова',
                reply_markup=await keyboards.functionals.cash_report.back_keyboard(data['point_name'])
            )
    else:
        await state.set_state(CashReportState.checks_file)
        message = await message.answer_photo(
            photo=types.FSInputFile('./files/Добавление файла.png')
        )
        await state.update_data(last_message_id=message.message_id)




@messages_router.message(CashReportState.enter_sum)
async def get_money_begin(message: types.Message, bot: Bot, state: FSMContext, sheet):
    data = await state.get_data()
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.delete_message(chat_id=message.chat.id, message_id=data['last_message_id'])
    if message.text.isdigit():
        day = datetime.strptime(data['date'], '%d.%m.%Y').timetuple().tm_yday
        try:
            sheet.values().update(
                spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
                range=f"{data['point_name']}!{data['data_cash']}{day + 1}",
                valueInputOption="USER_ENTERED",
                body={
                    'values': [[int(message.text)]]
                }
            ).execute()
            items = keyboards.functionals.cash_report.data_cash_report_keyboard
            for item in items:
                if item['callback'] == data['callback_data']:
                    await cash_report_service.create({
                        'name': f"{item['name']}",
                        'createAt': datetime.strptime(data['date'], '%d.%m.%Y').isoformat(),
                        'point': int(data['id_point']),
                    })
            await message.answer_photo(
                photo=types.FSInputFile('./files/Кассовый отчет главная.png'),
                reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(current_page=0,
                                                                                          day=data['day'],
                                                                                          mouth=data['mouth'],
                                                                                          year=data['year'],
                                                                                          point_name=data['point_name'])
            )
        except Exception as e:
            print(e)
            await message.answer(
                'Произошла ошибка 🚫\n'
                '\nПопробуйте снова',
                reply_markup=await keyboards.functionals.cash_report.back_keyboard(data['point_name'])
            )
    else:
        await state.set_state(CashReportState.enter_sum)
        message = await message.answer_photo(
            photo=types.FSInputFile('./files/Указание суммы.png')
        )
        await state.update_data(last_message_id=message.message_id)


@messages_router.message(CashReportState.comment)
async def get_comment(message: types.Message, bot: Bot, state: FSMContext, sheet):
    data = await state.get_data()
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.delete_message(chat_id=message.chat.id, message_id=data['last_message_id'])
    if message.text:
        day = datetime.strptime(data['date'], '%d.%m.%Y').timetuple().tm_yday
        try:
            sheet.values().update(
                spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
                range=f"{data['point_name']}!{data['data_cash']}{day + 1}",
                valueInputOption="USER_ENTERED",
                body={
                    'values': [[message.text]]
                }
            ).execute()
            items = keyboards.functionals.cash_report.data_cash_report_keyboard
            for item in items:
                if item['callback'] == data['callback_data']:
                    await cash_report_service.create({
                        'name': f"{item['name']}",
                        'createAt': datetime.strptime(data['date'], '%d.%m.%Y').isoformat(),
                        'point': int(data['id_point']),
                    })
            await message.answer_photo(
                photo=types.FSInputFile('./files/Кассовый отчет главная.png'),
                reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(current_page=0,
                                                                                          day=data['day'],
                                                                                          mouth=data['mouth'],
                                                                                          year=data['year'],
                                                                                          point_name=data['point_name'])
            )
        except Exception as e:
            print(e)
            await message.answer(
                'Произошла ошибка 🚫\n'
                '\nПопробуйте снова',
                reply_markup=await keyboards.functionals.cash_report.back_keyboard(data['point_name'])
            )
    else:
        await state.set_state(CashReportState.enter_sum)
        message = await message.answer_photo(
            photo=types.FSInputFile('./files/Указание суммы.png')
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
        await message.answer_photo(
            photo=types.FSInputFile('./files/Кассовый отчет главная.png'),
            reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(0)
        )
    else:
        await state.set_state(CashReportState.collected_fullname)
        message = await message.answer_photo(
            photo=types.FSInputFile('./files/Ввод ФИО.png')
        )
        await state.update_data(last_message_id=message.message_id)