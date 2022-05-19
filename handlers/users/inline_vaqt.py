from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default.Viloyatlar import viloyat
from loader import dp


# Echo bot
@dp.callback_query_handler(text='vaqt')
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text='Viloyatlarni tanlang',reply_markup=viloyat)