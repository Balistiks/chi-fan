from datetime import datetime

from aiogram import Bot, types
from aiohttp import web

import pandas as pd

from web.misc.configuration import conf
from web import keyboards
from web.services import users_service



routes = web.RouteTableDef()

bot = Bot(conf.bot.token)


@routes.post('web/users/date')
async def send_swap(request):
    auth = request.headers['Authorization']
    if auth.split(' ')[0] == 'Bearer':
        token = auth.split(' ')[1]
        if token == conf.bot.secret_token:
            data = await request.json()
            user_scheduleForSwap = data['scheduleForSwap']
            user_mainSchedule = data['mainSchedule']

            user_swap = await users_service.get_by_name(user_scheduleForSwap['name'])
            user_main = await users_service.get_by_name(user_mainSchedule['name'])

            user_id_swap = user_swap['tgId']
            user_id_main = user_main['tgId']

            date_string = user_mainSchedule['date']
            date_object = datetime.strptime(date_string, '%Y-%m-%d')
            formatted_date = date_object.strftime('%d.%m.%Y')

            await bot.send_message(
                chat_id=user_id_swap,
                text=f'С тобой хочет замениться:\n\n'
                      f'- {user_mainSchedule["name"]}\n- {formatted_date}\n- {user_mainSchedule['point']['name']}\n- '
                     f'{user_mainSchedule['startTime']} - {user_mainSchedule['endTime']}',
                reply_markup=await keyboards.swap_keyboard(user_id_main, user_mainSchedule['id'], user_scheduleForSwap['id'])
            )
            return web.Response()
    return web.Response(status=403)
