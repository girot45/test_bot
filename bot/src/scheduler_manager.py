from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.bot_manager import bot
from bot.handlers.text_answers import send_table_today_or_tomorrow


scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


def turn_on_schedule_for_user(
        tgid: int
):
    scheduler.add_job(
        send_table_today_or_tomorrow,
        'cron',
        id=f"{tgid}mo",
        day_of_week='mon-sun',
        seconds=300,
        kwargs={'message': bot, 'chat_id': tgid, 'istomorrow': False},
        max_instances=5)


def turn_of_schedule_for_user(tgid: int):
    scheduler.remove_job(job_id=f"{tgid}ev")
    scheduler.remove_job(job_id=f"{tgid}mo")