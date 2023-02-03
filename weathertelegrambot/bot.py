import logging

from aiogram import Bot, Dispatcher

from . import handlers


logging.basicConfig(
	level = logging.INFO,
	format = u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s' 
)
logger = logging.getLogger(__name__)


async def run(token: str):
	bot = Bot(token)
	dp = Dispatcher(bot)

	handlers.register(dp)

	logger.info('Starting bot')
	await dp.start_polling()