from aiogram.filters.callback_data import CallbackData


class ChooseLang(CallbackData, prefix='choose_lang'):
    lang: str