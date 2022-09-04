from KawaiiXRobot import bot, KAWAII_LOGS, DEVS, Inspector, KAWAII_CHANNEL, ubot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
import time
from pyrogram.types import Message
from KawaiiXRobot.utils.dbfunctions import (
    add_gban_user, remove_gban_user
)

OWO = DEVS + Inspector


@bot.on_message(filters.command("scan"))
async def scanning(_, message):
         global user_id
         if message.from_user.id not in OWO:
              return await message.reply_text("Sorry bitch your not my own user") 
         if not message.command[1]:
                  await message.reply("*Any reason to scanning?")
         elif message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                admire = message.from_user.id
                reason = message.command[1] 
         msg = await message.reply_text("**Connecting to Cringe System...**")
         await add_gban_user(user_id)
         text = f""" **From Chat:** {message.chat.title}
**Admire:** [{admire}](tg://user?id={admire})
**Scanned:** [{user_id}](tg://user?id={user_id})"""

         await ubot.send_message(-1001781501832, f"/gban {user_id}")
         Button = [[ InlineKeyboardButton(text="revert", callback_data="unscan")]]
         await bot.send_message(-1001781501832, text,
         reply_markup=InlineKeyboardMarkup(Button))
         await msg.edit(f"Successfully Scanned [{user_id}]({tg://user?id={user_id}) ")
         
                
@bot.on_callback_query(filters.regex("unscan"))
async def unscan(_, query):
       if query.from_user.id in OWO:
           await remove_gban_user(user_id)
           await ubot.send_message(-1001781501832, f"/ungban {user_id}")
           text = f""" **From Chat:** {query.message.chat.title}
**Admire:** [{query.from_user.id}](tg://user?id={query.from_user.id})
**Scanned:** [{user_id}](tg://user?id={user_id})"""
           await  bot.send_message(-1001781501832, text)
           await query.message.edit("unscanned")

