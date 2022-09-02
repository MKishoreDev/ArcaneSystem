from KawaiiXRobot import bot, KAWAII_LOGS, DEVS, Inspector, KAWAII_CHANNEL, ubot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
import time
from pyrogram.types import Message
from KawaiiXRobot.utils.dbfunctions import (
    add_gban_user,
)

OWO = DEVS + Inspector

@bot.on_message(filters.command("scan"))
async def scan(_, message):
        if not message.from_user.id in OWO:
               return await message.reply("Only owo users can scan")
        elif len(message.command) <2:
                  return await message.reply("give user ID")
        elif len(message.command) <3:
                  await message.reply("give reason to scan")
         uid = message.text.split(None, 1)[1]
         user = await bot.get_users(uid)
         reason = message.text.split(None, 2)[2]
        elif user.id in OWO:
              return await message.reply("WTF you can't scan fight with another owo user")
        await add_gban_user(user.id)
        await bot.send_message(message.chat.id,
                    f"""
#BANNED
**USER**: [{user}](tg://user?id={user.id})
**REASON**: {reason}
**ENFORCER**: [{enforcer}](tg://user?id={message.from_user.id})
**CHAT_ID** : {message.chat.id}
""")
   

