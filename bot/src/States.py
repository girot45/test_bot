from aiogram.filters.state import StatesGroup, State

class InputCardState(StatesGroup):
    cardNum = State()
