from aiogram.fsm.state import StatesGroup, State


class NewEmployeeState(StatesGroup):
    tg_id = State()
    name = State()