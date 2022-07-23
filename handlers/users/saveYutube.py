import requests
from pytube import YouTube
from aiogram import types
from filters.user import user
from loader import dp, bot
from aiogram.types import ContentType


@dp.message_handler(user(), content_types=ContentType.TEXT)
async def bot_echo(message: types.Message):
    my_video = YouTube(message.text)
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

    querystring = {"videoId": my_video.video_id, "lang": "uz", "videos": "true", "audios": "true", "subtitles": "true"}

    headers = {
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com",
        "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    t = response.json()['title']
    v = response.json()['videos']['items'][0]['url']

    await bot.send_video(chat_id=message.chat.id,
                         caption=f'{t}\n\nhttps://t.me/YouTubeApp_bot orqali video yuklab oling', video=v)

    print(response.text)
