from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.managers.bot_manager import bot
from bot.src.scripts.send_card_by_notif import sub_card_number

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
job_registry = {}

def turn_on_schedule_for_user(
        tgid: int,
        card_id
):
    global job_registry

    if job_registry.get(tgid) is not None:
        job_registry[tgid].add(card_id)
    else:
        job_registry[tgid] = {card_id}
    if scheduler.get_job(job_id=f"{tgid}_{card_id}fivemin") is None:
        scheduler.add_job(
            sub_card_number,
            'interval',
            id=f"{tgid}_{card_id}fivemin",
            seconds=15,
            kwargs={'bot': bot, 'chat_id': tgid, 'item_id': card_id},
            max_instances=5)


def turn_off_schedule_for_user(tgid: int):
    global job_registry
    if job_registry.get(tgid) is not None:
        for item in job_registry[tgid]:
            scheduler.remove_job(job_id=f"{tgid}_{item}fivemin")
        job_registry.pop(tgid)
