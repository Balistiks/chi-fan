from aiogram.fsm.state import StatesGroup, State


class CashReportState(StatesGroup):
    morning_recount = State()
    money_begin = State()
    collected_fullname = State()