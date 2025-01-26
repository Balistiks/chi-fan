import asyncio
import logging
import sys

from aiogram import Bot
from openai import OpenAI


from redis.asyncio.client import Redis

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler_di import ContextSchedulerDecorator

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from google.oauth2.credentials import Credentials as CredentialsClient

from bot.scheduler import schedule_opening_shift, schedule_closing_shift

from bot.misc.configuration import conf

from bot.dispatcher import get_redis_storage, get_dispatcher


async def start_bot():
    bot = Bot(conf.bot.token)
    print(conf.redis.passwd)
    print(conf.redis.host)
    storage = get_redis_storage(
        redis=Redis(
            host=conf.redis.host,
            password=conf.redis.passwd,
            port=conf.redis.port,
        )
    )
    openai_client = OpenAI(api_key=conf.openai.api_key)

    job_stores = {
        'default': RedisJobStore(
            jobs_key='dispatched_trips_jobs',
            run_times_key='dispatched_trips_running',
            host=conf.redis.host,
            port=conf.redis.port,
            password=conf.redis.passwd,
        )}
    scheduler = ContextSchedulerDecorator(AsyncIOScheduler(jobstores=job_stores))
    scheduler.ctx.add_instance(bot, declared_class=Bot)

    dp = get_dispatcher(storage=storage, scheduler=scheduler)

    credentials = Credentials.from_service_account_file(
        'files/token.json',
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
    )
    drive_service = build('drive', 'v3', credentials=credentials)
    sheets_service = build('sheets', 'v4', credentials=credentials)

    scheduler_static = AsyncIOScheduler(timezone='Asia/Vladivostok')
    scheduler_static.add_job(
        schedule_opening_shift,
        trigger='cron',
        hour='*',
        kwargs={'bot': bot, 'apscheduler': scheduler_static, 'storage': storage}
    )
    scheduler_static.add_job(
        schedule_closing_shift,
        trigger='cron',
        hour='*',
        kwargs={'bot': bot, 'apscheduler': scheduler_static, 'storage': storage}
    )

    sheet = sheets_service.spreadsheets()
    files = drive_service.files()

    scheduler.start()
    scheduler_static.start()
    await dp.start_polling(
        bot,
        sheet=sheet,
        files=files,
        allowed_updates=dp.resolve_used_update_types(),
        openai_client=openai_client
    )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start_bot())