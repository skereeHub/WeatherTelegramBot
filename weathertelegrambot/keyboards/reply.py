from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


MenuKeyboard = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = 'Get weather')
		],
		[
			KeyboardButton(text = 'Set weather', request_location = True)
		]
	]
)