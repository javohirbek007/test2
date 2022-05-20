import requests
from aiogram import types

from loader import dp,bot
@dp.message_handler(text='Guliston')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=guliston"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )



@dp.message_handler(text='Qarshi')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=qarshi"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )

@dp.message_handler(text='Urganch')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=urganch"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text='Termiz')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=termiz"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text='Nukus')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=nukus"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text='Xiva')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=xiva"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text='Andijon')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Andijon"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text='Buxoro')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Buxoro"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text="Farg'ona")
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Fergana"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Farg'оna"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text='Jizzax')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Jizzax"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text='Namangan')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Namangan"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text='Navoiy')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Navoiy"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text='Samarqand')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Samarqand"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )
@dp.message_handler(text='Toshkent')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Toshkent"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Toshkent"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']
  region = response.json()['region']

  user_id = message.from_user.id
  await message.answer(text=f"🔻 Namoz vaqtlari:{region}"
                            f"\n\n🌅Quyosh -{quyosh_chiqishi}"
                            f"\n🕰Tong - {bomdod}"
                            f"\n🕰Peshin vaqti - {peshin}"
                            f"+'\n🕰Asr vaqti - {asr}"
                            f"\n🕰Shom vaqti - {shom}"
                            f"\n🕰Xufton vaqti - {xufton}"
                            f"\nBugun - {kun}"
                            f"\nHijriy {hijri_vaqt}\n{hijr_oy} oyning, {hafta_kuni_hijri} kuni"
                            f"\nHaftaning {hafta_kuni} kuni"
                            )



@dp.message_handler(text='👨🏻‍💻 Dasturchi')
async def bot_echo(message: types.Message):
    await message.answer(text=f"👨🏻‍💻 Dasturchi - @JAVOHIR_NABIYEV \n\n\n\n➖➖➖➖➖➖➖➖➖")



