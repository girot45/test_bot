from aiogram import Bot

from bot.src.database import db_connect
from bot.src.scripts.db_scripts import insert_user_query
from bot.src.scripts.wb import get_card_info


async def sub_card_number(
        bot: Bot,
        chat_id,
        item_id
):
    session = await db_connect.get_session()
    result = get_card_info(item_id)
    if result is None:
        await bot.send_message(chat_id, "Такого товара нет")
        return
    qty, rating, name, price, card_id = result
    await insert_user_query(
        session,
        chat_id,
        int(item_id)
    )
    mes = f"Название товара: {name}\nЦена: {price}\nАртикул: {card_id}\nРейтинг: {rating}\nОстаток: {qty}"
    await bot.send_message(
            chat_id,
            mes
        )
