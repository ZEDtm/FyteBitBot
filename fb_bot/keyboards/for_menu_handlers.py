from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from fb_bot.config import LANG
from fb_bot.call_data.for_menu_handlers import ChooseLang, AskAQuestion, TechnicalTask, Cancel


def start_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=LANG['ask_a_question_keyboard'][lang], callback_data=AskAQuestion(ask=True))
    keyboard.button(text=LANG['technical_task_keyboard'][lang], callback_data=TechnicalTask(task=True))
    if lang == 'ru':
        keyboard.button(text='English', callback_data=ChooseLang(lang='en'))
    else:
        keyboard.button(text='Русский', callback_data=ChooseLang(lang='ru'))
    keyboard.adjust(1)
    return keyboard.as_markup()


def question_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=LANG['cancel_keyboard'][lang], callback_data=Cancel(cancel=True))
    keyboard.adjust(1)
    return keyboard.as_markup()