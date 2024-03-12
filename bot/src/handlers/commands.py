from aiogram import types, Router
from aiogram.filters import Command

from bot.src.database import db_connect
from bot.src.handlers.keyboards import main_menu_buttons

router_commands = Router()

@router_commands.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Добро пожаловать!!! Этот бот поможет вам с получением "
        "информации о карточках в wildberries.",
        reply_markup=main_menu_buttons()
    )
