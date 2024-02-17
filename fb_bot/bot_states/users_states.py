from aiogram.fsm.state import StatesGroup, State


class AskAQuestionState(StatesGroup):
    ask = State()


class TechnicalAssignmentState(StatesGroup):
    purpose = State()
    general = State()
    gui = State()
    parameters = State()
    specifications = State()
    end = State()
