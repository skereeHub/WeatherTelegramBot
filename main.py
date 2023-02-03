import asyncio
import os
from dotenv import load_dotenv

from weathertelegrambot import run


load_dotenv()


if __name__ == '__main__':
	task = run(token = os.getenv('TELEGRAM_BOT_TOKEN'))
	asyncio.run(task)