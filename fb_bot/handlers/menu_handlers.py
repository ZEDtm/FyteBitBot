import asyncio

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from fb_bot.call_data.for_menu_handlers import ChooseLang, AskAQuestion, Cancel, TechnicalTask
from fb_bot.database.collection import users_db
from fb_bot.keyboards.for_menu_handlers import start_keyboard, question_keyboard
from fb_bot.bot_states.users_states import AskAQuestionState, TechnicalAssignmentState
from fb_bot.config import LANG

router = Router(name='main')


@router.message(Command("start"))
async def command_start(message: Message, user: dict) -> None:
    text = LANG['start'][user['lang']].format(name=message.from_user.first_name)
    print(message.chat.id)
    await message.answer(text, reply_markup=start_keyboard(user['lang']))


@router.callback_query(ChooseLang.filter())
async def choose_lang(call: CallbackQuery, callback_data: ChooseLang, user: dict) -> None:
    lang = callback_data.lang
    users_db.update_one(user, {'$set': {'lang': lang}})
    user['lang'] = lang
    await call.message.answer(LANG['choose_lang'][user['lang']])


@router.callback_query(AskAQuestion.filter())
async def ask_a_question(call: CallbackQuery, state: FSMContext, user: dict) -> None:
    await state.set_state(AskAQuestionState.ask)
    await call.message.answer(LANG['ask_a_question'][user['lang']], reply_markup=question_keyboard(user['lang']))


@router.callback_query(TechnicalTask.filter())
async def technical_task(call: CallbackQuery, state: FSMContext, user: dict) -> None:
    await state.set_state(TechnicalAssignmentState.purpose)
    await call.message.answer(LANG['technical_purpose'][user['lang']], reply_markup=question_keyboard(user['lang']))


@router.callback_query(Cancel.filter(), StateFilter(AskAQuestionState.ask, TechnicalAssignmentState))
async def cancel_handler(call: CallbackQuery, state: FSMContext, user: dict) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    text = LANG['start'][user['lang']].format(name=call.from_user.first_name)
    await call.message.answer(text, reply_markup=start_keyboard(user['lang']))