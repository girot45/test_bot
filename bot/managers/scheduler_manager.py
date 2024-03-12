from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.managers.bot_manager import bot
from bot.src.scripts.wb import get_card_info

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
job_registry = {}

def turn_on_schedule_for_user(
        tgid: int,
        card_id
):
    global job_registry
    if job_registry.get(tgid) is not None:
        job_registry[tgid].append(card_id)
    else:
        job_registry[tgid] = [card_id]
    scheduler.add_job(
        get_card_info,
        'cron',
        id=f"{tgid}_{card_id}fivemin",
        day_of_week='mon-sun',
        seconds=300,
        kwargs={'message': bot, 'chat_id': tgid, 'istomorrow': False},
        max_instances=5)



def turn_off_schedule_for_user(tgid: int):
    global job_registry
    if job_registry.get(tgid) is not None:
        for item in job_registry[tgid]:
            scheduler.remove_job(job_id=f"{tgid}_{item}fivemin")
        job_registry.pop(tgid)
