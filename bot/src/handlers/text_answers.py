from typing import Optional

from aiogram import types, F, Router, Bot
from aiogram.fsm.context import FSMContext

from bot.src.States import InputCardState
from bot.src.database import db_connect
from bot.managers.scheduler_manager import turn_off_schedule_for_user
from bot.src.handlers.keyboards import sub_button
from bot.src.scripts.db_scripts import insert_user_query, \
    get_last_5_queries
from bot.src.scripts.util import proccess_info_from_db
from bot.src.scripts.wb import get_card_info

router_text = Router()


@router_text.message(
    F.text == "Остановить уведомления"
)
async def turn_off_notif(message: types.Message):
    turn_off_schedule_for_user(message.from_user.id)
    await message.answer("Все уведомления остановлены")


@router_text.message(
    F.text == "Получить информацию из БД"
)
async def answer_info_from_bd(message: types.Message):
    session = await db_connect.get_session()
    result = await get_last_5_queries(session)
    res = proccess_info_from_db(result)
    await message.answer(res)


@router_text.message(
    F.text == "Получить информацию по товару"
)
async def answer_card_info(message: types.Message, state: FSMContext):
    await message.answer("Введите номер карточки")
    await state.set_state(InputCardState.cardNum)


@router_text.message(
    InputCardState.cardNum,
    F.text.regexp("[0-9]+")
)
async def answer_card_number(
        message: Optional[Bot | types.Message],
        chat_id: Optional[int] = None,
        item_id: Optional[int] = None
):
    message_type = type(message)

    session = await db_connect.get_session()
    result = get_card_info(message.text)
    if result is None:
        if message_type == Bot:
            await message.send_message(chat_id, "Такого товара нет")
        else:
            await message.answer("Такого товара нет")
        return
    qty, rating, name, price, card_id = result
    await insert_user_query(
        session,
        message.from_user.id,
        int(message.text)
    )
    mes = f"Название товара: {name}\nЦена: {price}\nАртикул: {card_id}\nРейтинг: {rating}\nОстаток: {qty}"
    if message_type == Bot:
        await message.send_message(
            chat_id,
            mes,
            reply_markup=sub_button(item_id).as_markup()
        )
    else:
        await message.answer(
            mes,
            reply_markup=sub_button(message.text).as_markup()
        )
