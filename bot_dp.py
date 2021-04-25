from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token="1690412141:AAFtFrjXpiqPI9V3neXx3kMsmCTUCprXa2I")
dp = Dispatcher(bot, storage=storage)
