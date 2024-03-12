import asyncio

from bot.managers.bot_manager import dp, bot
from bot.managers.log_manager import logger
from bot.managers.scheduler_manager import scheduler
from bot.src.handlers.callback import router_callback
from bot.src.handlers.commands import router_commands
from bot.src.handlers.text_answers import router_text


dp.include_routers(router_commands, router_text, router_callback)


async def main():
    scheduler.start()
    await dp.start_polling(bot)


try:
    asyncio.run(main())
except Exception:
    import traceback
    logger.warning(traceback.format_exc())
