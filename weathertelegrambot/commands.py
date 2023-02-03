from aiogram import Bot
from aiogram.types import BotCommand


WeatherCommand = BotCommand('weather', 'показывает погоду в заданом городе')


async def register(bot: Bot):
	await bot.set_my_commands(
		[
			WeatherCommand
		]
	)