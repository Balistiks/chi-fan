import re
from datetime import datetime

from aiogram import Router, types, Bot
from aiogram.fsm.context import FSMContext
from googleapiclient.http import MediaIoBaseUpload

from bot.misc import functions
from bot.services import users_service
from bot.states import CashReportState
from bot import keyboards

messages_router = Router()


@messages_router.message(CashReportState.recount)
async def get_morning_recount(message: types.Message, bot: Bot, state: FSMContext, files, sheet):
    data = await state.get_data()
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=data['last_message_id'])

    if message.video:
        now_day = datetime.today().timetuple().tm_yday
        user = await users_service.get_by_tg_id(message.from_user.id)
        file = await bot.get_file(message.video.file_id)
        video = await bot.download_file(file.file_path)
        media = MediaIoBaseUpload(video, mimetype='video/mp4')
        parent = '1R45RY17a1ZllY8IR_s4HcTmdSifScCzh' \
            if data['recount_data'] == 'K' else '1biqIsDTb9cXCdmZrlmZ1hJv05QA9_Vtp'
        resp = files.create(
            body={
                'name': f'{datetime.today().strftime("%d.%m.%Y")}.mp4',
                'parents': [parent]
            },
            media_body=media,
            fields='id'
        ).execute()
        sheet.values().update(
            spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
            range=f"{user['point']['name']}!{data['recount_data']}{now_day + 1}",
            valueInputOption="USER_ENTERED",
            body={
                'values': [[f'https://drive.google.com/file/d/{resp["id"]}']]
            }
        ).execute()
        await message.answer(
            text='Кассовый отчет',
            reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(data.get('current_page', 0))
        )
    else:
        await state.set_state(CashReportState.recount)
        message = await message.answer(
            text='Прикрепите видео'
        )
        await state.update_data(last_message_id=message.message_id)


@messages_router.message(CashReportState.checks_file)
async def get_checks_file(message: types.Message, bot: Bot, state: FSMContext, files, sheet):
    data = await state.get_data()
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=data['last_message_id'])

    if message.document:
        now_day = datetime.today().timetuple().tm_yday
        user = await users_service.get_by_tg_id(message.from_user.id)
        file = await bot.get_file(message.document.file_id)
        document = await bot.download_file(file.file_path)
        media = MediaIoBaseUpload(document, mimetype='application/pdf')
        parent = '1XIzUDEx_RhkrfRPzfCXdkClmDEQ3aST-'
        resp = files.create(
            body={
                'name': f'{datetime.today().strftime("%d.%m.%Y")}.pdf',
                'parents': [parent]
            },
            media_body=media,
            fields='id'
        ).execute()
        sheet.values().update(
            spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
            range=f"{user['point']['name']}!{data['recount_data']}{now_day + 1}",
            valueInputOption="USER_ENTERED",
            body={
                'values': [[f'https://drive.google.com/file/d/{resp["id"]}']]
            }
        ).execute()
        await message.answer(
            text='Кассовый отчет',
            reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(data.get('current_page', 0))
        )
    else:
        await state.set_state(CashReportState.checks_file)
        message = await message.answer(
            text='Прикрепите файл'
        )
        await state.update_data(last_message_id=message.message_id)


@messages_router.message(CashReportState.enter_sum)
async def get_money_begin(message: types.Message, bot: Bot, state: FSMContext, sheet):
    data = await state.get_data()
    await functions.delete_message(bot=bot, chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.delete_message(chat_id=message.chat.id, message_id=data['last_message_id'])
    if message.text.isdigit():
        now_day = datetime.today().timetuple().tm_yday
        user = await users_service.get_by_tg_id(message.from_user.id)
        sheet.values().update(
            spreadsheetId='1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
            range=f"{user['point']['name']}!{data['data_cash']}{now_day+1}",
            valueInputOption="USER_ENTERED",
            body={
                'values': [[int(message.text)]]
            }
        ).execute()
        await message.answer(
            text='Кассовый отчет',
            reply_markup=await keyboards.functionals.cash_report.cash_report_keyboard(0)
        )
    else:
        await state.set_state(CashReportState.enter_sum)
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