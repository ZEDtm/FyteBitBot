import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext


from fb_bot.call_data.for_menu_handlers import ChooseLang, AskAQuestion, Cancel
from fb_bot.database.collection import users_db
from fb_bot.keyboards.for_menu_handlers import start_keyboard, question_keyboard
from fb_bot.bot_states.users_states import AskAQuestionState, TechnicalAssignmentState
from fb_bot.config import LANG, ADMIN_CHAT, bot
from fb_bot.custom_filters.for_technical_task_handlers import TextAndVoiceFilter

router = Router(name='ta')


@router.message(StateFilter(TechnicalAssignmentState.purpose))
async def purpose_question(message: Message, state: FSMContext, user: dict) -> None:
    await state.set_data({'task': message.text})
    await message.answer(LANG['technical_general'][user['lang']])
    await state.set_state(TechnicalAssignmentState.general)


@router.message(StateFilter(TechnicalAssignmentState.general))
async def general_question(message: Message, state: FSMContext, user: dict) -> None:
    data = await state.get_data()
    await state.set_data({'task': data['task'] + '\n' + message.text})
    await message.answer(LANG['technical_gui'][user['lang']])
    await state.set_state(TechnicalAssignmentState.gui)


@router.message(StateFilter(TechnicalAssignmentState.gui))
async def gui_question(message: Message, state: FSMContext, user: dict) -> None:
    data = await state.get_data()
    await state.set_data({'task': data['task'] + '\n' + message.text})
    await message.answer(LANG['technical_parameters'][user['lang']])
    await state.set_state(TechnicalAssignmentState.parameters)


@router.message(StateFilter(TechnicalAssignmentState.parameters))
async def parameters_question(message: Message, state: FSMContext, user: dict) -> None:
    data = await state.get_data()
    await state.set_data({'task': data['task'] + '\n' + message.text})
    await message.answer(LANG['technical_specifications'][user['lang']])
    await state.set_state(TechnicalAssignmentState.specifications)


@router.message(StateFilter(TechnicalAssignmentState.specifications))
async def specifications_question(message: Message, state: FSMContext, user: dict) -> None:
    data = await state.get_data()
    await state.set_data({'task': data['task'] + '\n' + message.text})
    await message.answer(LANG['technical_end'][user['lang']])
    await state.set_state(TechnicalAssignmentState.end)


@router.message(StateFilter(TechnicalAssignmentState.end))
async def end_question(message: Message, state: FSMContext, user: dict) -> None:
    data = await state.get_data()
    from fb_bot.modules.gigachat_module import get_text
    #text = f"{data['purpose']}\n{data['general']}\n{data['gui']}\n{data['parameters']}" \
    #       f"\n{data['specifications']}"
    await message.answer(await get_text("Составь техническое задание на основе этих данных (не пиши вступление)" + str(data)))
    await state.clear()