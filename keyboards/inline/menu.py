from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Nomoz Vaqtlari',callback_data='vaqt'),
            InlineKeyboardButton(text='Nomoz o\'qshni o\'rgansh',callback_data='Nomoz')
        ],

    ]
)