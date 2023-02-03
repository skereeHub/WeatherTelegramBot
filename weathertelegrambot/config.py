import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class Config:
	tg_token: str
	mongo_url: str
	weather_token: str


def load_config(path: str = None) -> Config:
	load_dotenv(path)
	return Config(
		tg_token = os.getenv('TELEGRAM_BOT_TOKEN'),
		mongo_url = os.getenv('MONGO_CONNECTION'),
		weather_token = os.getenv('WEATHER_TOKEN')
	)