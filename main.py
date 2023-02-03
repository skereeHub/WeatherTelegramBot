import asyncio

from weathertelegrambot import run


if __name__ == '__main__':
	task = run()
	asyncio.run(task)