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

@bot.on_message(filters.command("revert"))
async def revive(_, message):
          
          if message.from_user.id in OWO and message.reply_to_message:
                       await add_gban_user(message.reply_to_message.from_user.id)
                       await message.reply(f"Kawai User: {message.from_user.id}\n target user: {message.reply_to_message.from_user.id}\n **BANNED**")  
          
          else:
                if message.from_user.id not in OWO:
                      return await message("Only OWO user can use")
                elif len(message.command) <2:
                      return await message.reply("give a user ID or name")
                elif not message.reply_to_message:
                     user_id_text = message.text.split(None, 1)[1]
                     user = await bot.get_users(user_id_text)
                     await add_gban_user(user.id)
                     await message.reply(f"Kawai User: {message.from_user.id}\n target user: {user.id}\n **BANNED**")
             

