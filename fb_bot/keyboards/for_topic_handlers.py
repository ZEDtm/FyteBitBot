from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from fb_bot.config import LANG
from fb_bot.call_data.for_menu_handlers import AskAQuestion


def answer_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=LANG['answer_keyboard'][lang], callback_data=AskAQuestion(ask=True))
    keyboard.adjust(1)
    return keyboard.as_markup()