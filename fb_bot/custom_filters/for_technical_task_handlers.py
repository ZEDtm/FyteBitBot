
from aiogram.types import Message, ForumTopicClosed
from aiogram import Bot
from aiogram.filters import BaseFilter


class TextAndVoiceFilter(BaseFilter):

    async def __call__(self, message: Message, bot: Bot) -> bool:
        if not isinstance(message, Message):
            return False
        return True if message.text or message.voice else False