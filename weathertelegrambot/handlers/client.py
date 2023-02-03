from aiogram import Dispatcher
from aiogram.types import Message, ContentType
from aiogram.types.input_message_content import InputLocationMessageContent
from aiogram.dispatcher.filters import CommandStart

from ..keyboards import MenuKeyboard


async def start(message: Message):
	await message.reply(
		'Hello, you can set your location for view weather.',
		reply_markup = MenuKeyboard
	)

async def set_location(message: Message):
	lat = message.location.latitude
	lon = message.location.longitude
	print(lat, lon)


async def weather(message: Message):
	pass


def register(dp: Dispatcher):
	dp.register_message_handler(start, CommandStart())
	dp.register_message_handler(set_location, content_types = [ContentType.LOCATION])