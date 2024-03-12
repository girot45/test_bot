import asyncio

from bot.managers.bot_manager import dp, bot
from bot.managers.log_manager import logger
from bot.src.handlers.commands import router_commands
from bot.src.handlers.text_answers import router_text


dp.include_routers(router_commands, router_text)


async def main():
    await dp.start_polling(bot)


try:
    asyncio.run(main())
except Exception:
    import traceback
    logger.warning(traceback.format_exc())