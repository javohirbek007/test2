from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

from aiogram.types import CallbackQuery
from loader import dp
inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Nomoz Vaqtlari',callback_data='Vaqt'),
            InlineKeyboardButton(text='👨🏻‍💻 Dasturchi',url='https://t.me/JAVOHIR_NABIYEV')
        ],

    ]
)
