from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("СТВОРИТИ ПОСТ📄"))


wait_for_link = ReplyKeyboardMarkup(resize_keyboard=True)
wait_for_link.add(KeyboardButton("ВІДМІНИТИ❌"))


post_confirmation = ReplyKeyboardMarkup(resize_keyboard=True)
post_confirmation.add(KeyboardButton("ВІДПАВИТИ✅"))
post_confirmation.add(KeyboardButton("ВІДМІНИТИ❌"))
