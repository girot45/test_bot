from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_buttons() -> ReplyKeyboardMarkup:
    item_info = KeyboardButton(text="Получить информацию по товару")
    stop_notif = KeyboardButton(text="Остановить уведомления")
    info_from_bd = KeyboardButton(text="Получить информацию из БД")

    buttons = [
        [item_info],
        [info_from_bd],
        [stop_notif]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    return keyboard
