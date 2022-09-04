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
async def scanning(_, message):
         global user_id
         if message.from_user.id not in OWO:
              return await message.reply_text("Sorry bitch your not my own user") 
         if message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                admin = message.from_user.id
                reason = message.command[1] 
         msg = await message.reply_text("**Connecting to Cringe System...**")
          await add_gban_user(user_id)
          ubot.send_message(chat_id, message_text)
          bot.send_message(log_channel_id, message_text)
         await msg.edit("Successfully Scanned")
         
                
@bot.on_callback_query(filters.regex("unscan"))
async def unscan(_, query):
       await remove_gban_user(user_id)
        ubot.send_message(chat_id, message.text)
        bot.send_message(chat_id, message.text)
       await query.message.edit("unscanned"

