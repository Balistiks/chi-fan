from aiogram.fsm.state import StatesGroup, State


class CheckList(StatesGroup):
    photo = State()