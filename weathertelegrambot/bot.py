import logging

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from motor.motor_asyncio import AsyncIOMotorClient

from . import filters
from . import handlers
from . import commands
from .config import load_config


logging.basicConfig(
	level = logging.INFO,
	format = u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s' 
)
logger = logging.getLogger(__name__)


async def run():
	config = load_config()

	bot = Bot(config.tg_token, parse_mode = ParseMode.MARKDOWN_V2)
	dp = Dispatcher(bot)
	
	bot.config = config
	bot.database = AsyncIOMotorClient(config.mongo_url).WeatherTelegramBot
	await commands.register(bot)

	filters.register(dp)
	handlers.register(dp)

	logger.info('Starting bot')
	await dp.start_polling()