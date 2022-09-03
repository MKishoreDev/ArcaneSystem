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
                 return await message.reply("give reason to scan")
        elif not message.reply_to_message:
                 user_id_text = message.text.split(None, 1)[1]
                 user = await bot.get_users(user_id_text)
                 reason = message.text.split(None, 2)[2]
                 await add_gban_user(user.id)
        await bot.send_message(message.chat.id, "this means the users is scanned hacker add here text")
        else:
               if len(message.command) <2:
                       await ok.edit_text("give reason boi")
               reason = message.text.split(None, 1)[1]
               user_id = message.reply_to_message.from_user.id
               info = await bot.get_users(user_id)
               await add_gban_user(user.id)
               await bot.send_message(message.chat.id,
                    f"""
#BANNED
**USER**: [{user}](tg://user?id={info.id})
**REASON**: {reason}
**ENFORCER**: [{enforcer}](tg://user?id={message.from_user.id})
**CHAT_ID** : {message.chat.id}
""")
               
                    
            

