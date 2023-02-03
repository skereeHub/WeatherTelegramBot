from aiogram import Dispatcher

from . import admin
from . import client


def register(dp: Dispatcher):
	admin.register(dp)
	client.register(dp)