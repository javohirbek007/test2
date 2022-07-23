from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu import inline_menu
import states.holatlar
from states.holatlar import Forma

from loader import dp, db
from filters.admin import admin
from filters.user import user


@dp.message_handler(admin(), commands='start')
async def bot_start(message: types.Message):
    await message.answer(text=f'Salom {message.from_user.first_name} admin panelga otish uchun /panel ni bosing',
                         reply_markup=inline_menu)
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    username = message.from_user.username
    tg_id = message.from_user.id

    print(db.barcha_foydalanuvchilar())

    try:
        db.user_qoshish(ism=ism, familya=familya, username=username, tg_id=tg_id)

    except Exception as xatolik:
        print(xatolik)


@dp.message_handler(user(), commands='start')
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    username = message.from_user.username
    tg_id = message.from_user.id
    try:
        db.user_qoshish(ism=ism, familya=familya, username=username, tg_id=tg_id)

    except Exception as xatolik:
        print(xatolik)

    await message.answer(text=f'salom botga hush kelbsz {message.from_user.full_name}',
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text=f'Bolmlardan birini tanlang', reply_markup=inline_menu)
