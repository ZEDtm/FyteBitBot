import json

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')
MONGO_LOGIN = getenv('MONGO_LOGIN')
MONGO_PASS = getenv('MONGO_PASS')
ADMIN_CHAT = getenv('ADMIN_CHAT')
GIGA_TOKEN = getenv('GIGA_TOKEN')

with open('lang.json', 'rb') as f:
    LANG = json.load(f)


storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)
