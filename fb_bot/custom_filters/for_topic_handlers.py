from typing import Any, Union, Dict
from aiogram.types import Message, ForumTopicClosed
from aiogram import Bot
from aiogram.filters import BaseFilter


class TopicCreateFilter(BaseFilter):

    async def __call__(self, message: Message, bot: Bot) -> bool:
        if not isinstance(message, Message):
            return False

        return True if message.forum_topic_created else False


class TopicReopenFilter(BaseFilter):

    async def __call__(self, message: Message, bot: Bot) -> bool:
        if not isinstance(message, Message):
            return False

        return True if message.forum_topic_reopened else False


class TopicCloseFilter(BaseFilter):

    async def __call__(self, message: Message, bot: Bot) -> bool:
        if not isinstance(message, Message):
            return False

        return True if message.forum_topic_closed else False


class TopicMessageTextFilter(BaseFilter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        if not isinstance(message, Message):
            return False

        return True if message.is_topic_message and message.text else False


