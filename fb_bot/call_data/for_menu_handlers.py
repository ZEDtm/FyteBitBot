from aiogram.filters.callback_data import CallbackData


class ChooseLang(CallbackData, prefix='choose_lang'):
    lang: str


class AskAQuestion(CallbackData, prefix='ask_a_question'):
    ask: bool


class TechnicalTask(CallbackData, prefix='technical_task'):
    task: bool


class Cancel(CallbackData, prefix='cancel'):
    cancel: bool