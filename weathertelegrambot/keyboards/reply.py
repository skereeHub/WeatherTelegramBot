from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


MenuKeyboard = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = 'Яка погода?')
		],
		[
			KeyboardButton(text = 'Зберегти геолокацію', request_location = True)
		]
	],
	resize_keyboard = True
)