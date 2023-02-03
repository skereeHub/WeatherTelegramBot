from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart

from ..keyboards import MenuKeyboard


async def start(message: Message):
	await message.reply('Hello')


async def weather(message: Message):
	pass


def register(dp: Dispatcher):
	dp.register_message_handler(start, CommandStart)