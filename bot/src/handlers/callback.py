from aiogram import Router, F, types

from bot.managers.scheduler_manager import turn_on_schedule_for_user
router_callback = Router()


@router_callback.callback_query(F.data.startswith("sub_"))
async def handle_subscribe_click(query: types.CallbackQuery):
    card_id = query.data.split("sub_")[1]
    turn_on_schedule_for_user(query.from_user.id, card_id)
