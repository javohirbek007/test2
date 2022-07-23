from aiogram import types

from loader import dp
from keyboards.inline.menu import inline_menu

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(text='Bunday buyruq yoq')
