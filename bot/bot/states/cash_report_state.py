from aiogram.fsm.state import StatesGroup, State


class CashReportState(StatesGroup):
    recount = State()
    enter_sum = State()
    collected_fullname = State()
    checks_file = State()