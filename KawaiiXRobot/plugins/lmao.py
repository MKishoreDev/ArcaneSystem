import asyncio

from KawaiiXRobot.utils.dbfunctions import (
    add_gban_user, is_gbanned_user
)
from KawaiiXRobot import KAWAII_LOGS, bot, DEVS, Inspector
from pyrogram import filters

OWO = DEVS + Inspector

@bot.on_message(filters.command("fuck") & filters.user(OWO) & ~filters.forwarded)
async def _(_, message):
try:
  if len(message.command) <2:
     return await message.reply("give user ID")
  elif len(message.command) <3:
    return await message.reply("give reason to scan")
    reason = message.text.split(None, 2)[2]
  if message.reply_to_message:
         r_from_id = message.reply_to_message.from_user.id
  else:
         r_from_id = message.text.split(None, 1)[1]
         return
  if r_from_id in OWO:
         await message.reply_text("`Kelathu Punda Unga Appa Punda Da Adhu Epadi Nee Ban Pannuva`")
  if is_gbanned_user(r_from_id) == False:
         await bot.send_message(
            KAWAII_LOGS,
            "/gban [user](tg://user?id={}) {} By {}".format(r_from_id, reason, message.from_user.id)
         )
         await message.delete()
         await message.reply_text("**Gbanning...**")
         await asyncio.sleep(3.5)
         await message.reply_text("**Gbanned Succesfully**")
         await add_gban_user(r_from_id)
         await message.delete()
  else:
        await message.reply_text("I Have Seen This Sussy Baka Already")
except Exception as e:
        print(e)

@bot.on_message(filters.command("revive") & filters.forwarded)
async def _(_, message):
    if message.reply_to_message:
         r_from_id = message.reply_to_message.from_user.id
    else:
         r_from_id = len(message.command) <2
         await bot.send_message(
            KAWAII_LOGS,
            "/ungban [user](tg://user?id={}) By {}".format(r_from_id, message.from_user.id)
         )
    await message.delete()
    await message.reply_text("**UnGbanning...**")
    asyncio.sleep(3.5)
    await message.reply_text("**UnGbanned Succesfully**")
    await message.delete()
