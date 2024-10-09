from aiogram.fsm.state import StatesGroup, State

class Survey(StatesGroup):
    full_name = State()
    feedback = State()
    start = State()
    same = State()
    photo = State()
    restart = State()
    raspisanie = State()
    project = State()
    project_one = State()
    same_one = State()
    weather = State()
    kubic = State()
    project_on = State()
    parse = State()
    sam_name = State()
