from aiogram.fsm.state import StatesGroup, State


class GPTState(StatesGroup):
    gpt = State()