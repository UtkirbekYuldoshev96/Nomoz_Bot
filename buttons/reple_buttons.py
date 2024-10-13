from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_Keybord = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('ℹ️Bot haqida malumot'),
            KeyboardButton("📍Manzil tanlang")
        ]
    ],
    resize_keyboard=True
)

add_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Toshkent'),
            KeyboardButton('Qarshi')
        ],
        [
            KeyboardButton('Farg\'ona'),
            KeyboardButton('Namangan')
        ],
        [
            KeyboardButton('Andijon'),
            KeyboardButton('Guliston')
        ],
        [
            KeyboardButton('Jizzax'),
            KeyboardButton('Samarqand')
        ],
        [
            KeyboardButton('Termiz'),
            KeyboardButton('Buxoro')
        ],
        [
            KeyboardButton('Navoiy'),
            KeyboardButton('Xiva')
        ],
        [
            KeyboardButton('Nukus')
        ]
    ],
    resize_keyboard=True,
)