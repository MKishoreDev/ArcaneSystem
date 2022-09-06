# Enforcer.py ©Copyright By @NandhaXD Machan Remaked By @HMF_Owner_1

from KawaiiXRobot import bot, KAWAII_LOGS, Enforcer, Dev, inspector, KAWAII_CHANNEL, ubot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
import time
from pyrogram.types import Message
from KawaiiXRobot.utils.dbfunctions import (
    add_gban_user, remove_gban_user
)

OWO = Enforcer

@bot.on_message(filters.command(["scan"], ['/', ".", "?"]))
async def scanning(_, message):
         global user_id
         if message.from_user.id not in OWO:
              return await message.reply_text("Sorry bitch your not my own user") 
         if len(message.command) <2:
                  await message.reply("*Any reason to scanning?")
                  return 
         elif message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                admire = message.from_user.id
                reason = message.text.replace("/scan", "")
         msg = await message.reply_text("**Connecting to Cringe System...**")
         text = f""" **From Chat:** {message.chat.title}
**Enforcer:** [{admire}](tg://user?id={admire})
**Scanned:** [{user_id}](tg://user?id={user_id})
**Reason**: {reason}

Wait For Inspectors 
"""

         await ubot.send_message(-1001781501832, f"/gban {user_id} by [admire](tg://user?id={admire}) × {reason}")
         Button = [[ InlineKeyboardButton(text="Scan", callback_data="button_scan")]]
         await bot.send_message(-1001723857695, text, reply_markup=InlineKeyboardMarkup(Button))
         await msg.edit_text(f"Successfully Scanned [{user_id}](tg://user?id={user_id})")

                       
@bot.on_callback_query(filters.regex("unscan"))
async def unscan(_, query):
       if query.from_user.id in OWO:
           await remove_gban_user(user_id)
           await ubot.send_message(-1001781501832, f"/ungban {user_id}")
           text = f""" **From Chat:** {query.message.chat.title}
**Admire:** [{query.from_user.id}](tg://user?id={query.from_user.id})
**UnScanned:** [{user_id}](tg://user?id={user_id})"""
           await query.message.edit(text)

HMF = Dev + inspector

@bot.on_callback_query(filters.regex("button_scan"))
async def button_scan(_, query):
         global user_id
     if query.from_user.id in OWO:
         await add_gban_user(user_id)
         await ubot.send_message(-1001781501832, f"/gban {user_id}")
         text = f""" **From Chat:** {query.message.chat.title}
**Admire:** [{query.from_user.id}](tg://user?id={query.from_user.id})
**Scanned:** [{user_id}](tg://user?id={user_id})
**Reason**: {reason}"""
          await query.message.edit(text, reply_markup=InlineKeyboardMarkup(Button))

         Button = [[ InlineKeyboardButton(text="revert", callback_data="unscan")]]
