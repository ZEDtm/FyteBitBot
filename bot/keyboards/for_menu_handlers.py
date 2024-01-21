from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from config import LANG
from bot.calldata.calldata import ChooseLang


def start_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=LANG['ask_a_question'][lang], callback_data='ask_a_question')
    if lang == 'ru':
        keyboard.button(text='English', callback_data=ChooseLang(lang='en'))
    else:
        keyboard.button(text='Русский', callback_data=ChooseLang(lang='ru'))
    keyboard.adjust(1)
    return keyboard.as_markup()
