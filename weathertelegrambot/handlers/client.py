from aiogram import Dispatcher
from aiogram.types import Message, ContentType
from aiogram.dispatcher.filters import Command, CommandStart, Text
from aiogram.utils.markdown import escape_md

from ..keyboards import MenuKeyboard
from ..commands import WeatherCommand
from ..api import WeatherApi


async def start(message: Message):
	response = (
		(
		'Привіт, ти можеш прив\'язати геолокацію для швидкого перегляду погоди, '
		'використай кнопку `Зберегти геолокацію`'
	)
	)
	await message.reply(escape_md(response), reply_markup = MenuKeyboard)

async def set_location(message: Message):
	lat = message.location.latitude
	lon = message.location.longitude
	
	collection = message.bot.database.Location
	await collection.replace_one(
		{
			'_id': message.from_id
		},
		{
			'location': {
				'lat': lat,
				'lon': lon
			}
		},
		upsert = True
	)
	await message.reply('Збережено')


async def weather(message: Message):
	user_data = None
	city = message.get_args()

	if not city:
		collection = message.bot.database.Location
		user_data = await collection.find_one({'_id': message.from_id})

	if not city and user_data is None:
		response = (
			'Вкажіть назву міста або збережіть геолокацію '
			'за допомогою кнопки `Зберегти геолокацію`'
		)
		return await message.reply(escape_md(response))

	weather_api = WeatherApi(message.bot.config.weather_token)

	data = None
	if city:
		data = await weather_api.get(city = city)
	elif user_data is not None:
		lat, lon = user_data['location'].values()
		data = await weather_api.get(coord = [lat, lon])

	if data is None:
		response = f'Я не зміг знайти місто *{city}*'
		return await message.reply(escape_md(response))

	response = (
		'У місті {name}, {country} зараз {weather}\n\n'
		'Температура: **{temp:.0f}°C**\nВідчувається як: **{feels_like:.0f}°C**'
	).format(
		name = data['name'],
		country = data['sys']['country'],
		weather = data['weather'][0]['description'],
		temp = data['main']['temp'],
		feels_like = data['main']['feels_like']
	)
	await message.reply(escape_md(response))


def register(dp: Dispatcher):
	dp.register_message_handler(start, CommandStart())
	dp.register_message_handler(set_location, content_types = [ContentType.LOCATION])
	dp.register_message_handler(weather, Text('Яка погода?', ignore_case = True))
	dp.register_message_handler(weather, Command(WeatherCommand, ignore_case = True))