from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


MenuKeyboard = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = 'Get weather')
		],
		[
			KeyboardButton(text = 'Set location', request_location = True)
		]
	],
	resize_keyboard = True
)