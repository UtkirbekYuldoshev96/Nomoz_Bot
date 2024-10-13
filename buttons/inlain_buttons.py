from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

add_Buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Toshkent', callback_data='tosh'),
            InlineKeyboardButton(text='Qarshi', callback_data='qash'),
        ],
        [
            InlineKeyboardButton(text='Farg\'ona', callback_data='far'),
            InlineKeyboardButton(text='Namangan', callback_data='nam'),
        ],
        [
            InlineKeyboardButton(text='Andijon', callback_data='and'),
            InlineKeyboardButton(text='Sirdaryo', callback_data='sir'),
        ],
        [
            InlineKeyboardButton(text='Jizzax', callback_data='jizzax'),
            InlineKeyboardButton(text='Samarqand', callback_data='sam'),
        ],
        [
            InlineKeyboardButton(text='Surhandaryo', callback_data='surh'),
            InlineKeyboardButton(text='Buxoro', callback_data='buxoro'),
        ],
        [
            InlineKeyboardButton(text='Navoiy', callback_data='nav'),
            InlineKeyboardButton(text='Xorazm', callback_data='xor'),
        ],
        [
            InlineKeyboardButton(text='Qoraqalpoqig\'iston', callback_data='qora_qol'),
            InlineKeyboardButton(text="Toshkent vil.", callback_data='tosh_v')   
        ]
    ],
    row_width=2
)