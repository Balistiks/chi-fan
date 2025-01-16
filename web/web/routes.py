from aiogram import Bot, types
from aiohttp import web

import pandas as pd

from web.misc.configuration import conf



routes = web.RouteTableDef()

bot = Bot(conf.bot.token)


@routes.post('/users/date')
async def send_status(request):
    auth = request.headers['Authorization']
    if auth.split(' ')[0] == 'Bearer':
        token = auth.split(' ')[1]
        if token == conf.bot.secret_token:
            data = await request.json()
            user = data['user']

            columns = ['Имя', 'Номер', 'UserName', 'tgId', 'Вакансия']

            data_formatted = {
                'Имя': user['name'],
                'Номер': user['phoneNumber'],
                'UserName': user['userName'],
                'tgId': user['tgId'],
                'Вакансия': user['answers'][0]['stage']['course'][0]['name'],
            }

            for answer in user['answers']:
                if len(answer['text']) != 0:
                    data_formatted[answer['stage']['name']] = answer['text']
                    columns.append(answer['stage']['name'])

            df = pd.DataFrame(data_formatted, columns=columns, index=[0])
            file_name = f'Соискатель_{user["tgId"]}.xlsx'
            df.to_excel(file_name, index=False)

            await bot.send_document(
                data['user']['employee']['tgId'],
                types.FSInputFile(file_name),
                caption=f'Соискатель {data["user"]["name"]}:\n'
                f'Город: {user["city"]}\n'
                f'Телефон: {data["user"]["phoneNumber"]}\n'
                f'TG: @{data["user"]["userName"]}\n'
                f'\nВыбрал дату созвона: {data["date"]}'
            )
            return web.Response()
    return web.Response(status=403)
