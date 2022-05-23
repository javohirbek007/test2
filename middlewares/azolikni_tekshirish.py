# from aiogram import types
# from aiogram.dispatcher.handler import CancelHandler
# from aiogram.dispatcher.middlewares import BaseMiddleware
#
# from data.config import kanalar
# from utils import majburiy_azolik
# from loader import bot
#
# class Asosiy_chesking(BaseMiddleware):
#     async def on_pre_process_update(self, xabar:types.Update, data:dict):
#         if xabar.message:
#             user_id = xabar.message.from_user
#         elif xabar.callback_query:
#             user_id = xabar.callback_query.from_user.id
#         else:
#             return
#         matn ="Quydagi kanalga azo bo'olin"
#         dastlabki_holat = True
#         for k in kanalar:
#             holat = await majburiy_azolik.tekshirish(user_id=user_id,kanal=k)
#             dastlabki_holat *= holat
#
#             kanal = await bot.get_chat(k)
#             if not holat:
#                 link = await kanal.export_invite_link()
#                 matn+=(f"👉<a href='{link}'>{kanal.title}</a>\n")
#         if not dastlabki_holat:
#             await xabar.message.answer(matn,disable_web_page_preview=True,)
#             raise CancelHandler()