import asyncio

from fb_bot.config import bot, dp
from fb_bot.middleware.usercheck_middlware import UserCheckMessageMiddleware, UserCheckCallbackMiddleware
from fb_bot.handlers import menu_handlers, topic_handlers, technical_task_handlers

import logging


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d - %(message)s')

    dp.include_routers(topic_handlers.router)


    dp.message.middleware.register(UserCheckMessageMiddleware())
    dp.callback_query.middleware.register(UserCheckCallbackMiddleware())

    dp.include_routers(technical_task_handlers.router)
    dp.include_routers(menu_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
