import sys

import aiogram
import aiohttp

from . import __version__


class WeatherApi:
	def __init__(self, token: str) -> None:
		self.token = token
		self.headers = {
			'User-Agent': 'TelegramBot (https://github.com/skereeHub/WeatherTelegramBot {0}) '\
				'Python/{1[0]}.{1[1]} aiogram/{2}'.format(__version__, sys.version_info, aiogram.__version__)
		}
	
	async def get(self, *, city: str = None, coord: list[float] = None):
		url = 'https://api.openweathermap.org/data/2.5/weather'
		
		params = {
			'appid': self.token,
			'lang': 'ua',
			'units': 'metric'
		}
		if city is not None:
			params['q'] = city
		elif coord is not None:
			lat, lon = coord
			params['lat'] = lat
			params['lon'] = lon
		
		async with aiohttp.ClientSession(headers = self.headers) as session:
			async with session.get(url, params = params) as response:
				return await response.json()