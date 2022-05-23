from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.Viloyatlar import viloyat
from keyboards.inline.menu import inline_menu

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text= f'salom botga hush kelbsz {message.from_user.full_name} Bolmlardan birini tanlang',reply_markup=inline_menu)
