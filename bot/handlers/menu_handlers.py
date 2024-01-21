from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from bot.calldata.calldata import ChooseLang
from bot.database.collection import users_db
from bot.keyboards.for_menu_handlers import start_keyboard
from bot.config import LANG

router = Router()


@router.message(Command("start"))
async def command_start(message: Message, user: dict) -> None:
    text = LANG['start'][user['lang']].format(name=message.from_user.first_name)
    await message.answer(text, reply_markup=start_keyboard(user['lang']))


@router.callback_query(ChooseLang.filter())
async def command_start(call: CallbackQuery, callback_data: ChooseLang, user: dict) -> None:
    lang = callback_data.lang
    users_db.update_one(user, {'$set': {'lang': lang}})
    user['lang'] = lang
    await call.message.answer(LANG['choose_lang'][user['lang']])
