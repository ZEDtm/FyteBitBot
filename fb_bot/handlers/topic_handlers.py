import re

from aiogram import Router
from aiogram.types import Message
from aiogram.exceptions import TelegramForbiddenError
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from fb_bot.bot_states.users_states import AskAQuestionState
from fb_bot.config import LANG, ADMIN_CHAT, bot
from fb_bot.keyboards.for_topic_handlers import answer_keyboard
from fb_bot.custom_filters.for_topic_handlers import TopicCreateFilter, TopicCloseFilter, TopicMessageTextFilter
from fb_bot.database.models import User
from fb_bot.modules import gigachat_module

router = Router(name='topic')


@router.message(StateFilter(AskAQuestionState.ask))
async def question_send(message: Message, state: FSMContext, user: dict) -> None:
    await state.clear()
    print(user['ticket'])
    if user['ticket']:
        await message.copy_to(chat_id=ADMIN_CHAT, message_thread_id=user['ticket'])
    else:
        result = await bot.create_forum_topic(chat_id=ADMIN_CHAT, name=f"Ticket #{message.from_user.id}")
        username = message.from_user.username
        text = "Новое обращение:\n"
        text += f'@{username}' if username \
            else f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
        await bot.send_message(chat_id=ADMIN_CHAT, text=text, message_thread_id=result.message_thread_id, parse_mode='HTML')
        await message.copy_to(chat_id=ADMIN_CHAT, message_thread_id=result.message_thread_id)
    await message.answer(LANG['ask_a_question_bot_answer'][user['lang']])


@router.message(TopicCreateFilter())
async def topic_create(message: Message) -> None:
    pattern = r"Ticket\s#(\d+)"
    if re.search(pattern, message.forum_topic_created.name):
        user_id = message.forum_topic_created.name.split(sep='#')[1]
        await User.set_ticket(message.message_thread_id, user_id)


@router.message(TopicCloseFilter())
async def topic_close(message: Message) -> None:
    user = await User.get_user_on_ticket(message.message_thread_id)
    if user:
        await User.delete_ticket(user['user_id'])


@router.message(TopicMessageTextFilter())
async def topic_message_handler(message: Message) -> None:
    if message.message_thread_id == 92:
        text = await gigachat_module.get_text(message.text)
        await message.answer(text)
    user = await User.get_user_on_ticket(message.message_thread_id)
    if user:
        try:
            await bot.send_message(user['user_id'], text=message.text, reply_markup=answer_keyboard(user['lang']))
        except TelegramForbiddenError:
            await message.answer('Пользователь заблокировал бота')
        return
