# Sacn.py ©Copyright By @NandhaXD Machan

import time
import pytz
import datetime
from Arcane import bot, KAWAII_LOGS, DEVS, Inspector, Enforcer, KAWAII_CHANNEL, ubot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
from pyrogram.types import Message
from Arcane.utils.dbfunctions import (
    add_gban_user, remove_gban_user
)


OWO = DEVS + Inspector 
HMF = Enforcer
COMMANDS = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]

india_Date_Time = datetime.datetime.now(tz=pytz.timezone("Asia/Calcutta"))
Current_Date_Time = india_Date_Time.strftime("%Y-%m-%dT%H:%M")

@bot.on_message(filters.command("scan", COMMANDS))
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

         if int(user_id) in DEVS:
             await message.reply_text(
                 "Dev's Can't Be Ban 😑"
             )
             return

         if int(user_id) in Inspector:
             await message.reply_text(
                 "Inspector's Can't Be Ban 😑"
             )
             return

         if int(user_id) in Enforcer:
             await message.reply_text(
                 "Enforcer's Can't Be Ban 😑. If You Want Ban Or Remove Enforcer Ask Dev With Correct Reason 👍"
             )
             return
                       
         msg = await message.reply_text("**Connecting to Cringe System...**")
         await add_gban_user(user_id)
         text = f""" **From Chat:** {message.chat.title}
**Admire:** [{admire}](tg://user?id={admire})
**Scanned:** [{user_id}](tg://user?id={user_id})
**Reason**: {reason}
**Event Stamp:** {Current_Date_Time}
"""

         await ubot.send_message(-1001781501832, f"/gban {user_id} {reason}")
         Button = [[ InlineKeyboardButton(text="revert", callback_data="bunscan")]]
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

# Enforcer Scan 

@bot.on_message(filters.command("escan"))
async def scanning(_, message):
         global user_id
         if message.from_user.id not in HMF:
              return await message.reply_text("Sorry bitch your not my own user") 
         if len(message.command) <2:
                  await message.reply("*Any reason to scanning?")
                  return 
         elif message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                admire = message.from_user.id
                reason = message.text.replace("/escan", "")
         msg = await message.reply_text("**Connecting to Cringe System...**")
         text = f""" **From Chat:** {message.chat.title}
**Enforcer:** [{admire}](tg://user?id={admire})
**Scanned:** [{user_id}](tg://user?id={user_id})
**Reason**: {reason}
**Event Stamp:** {Current_Date_Time}

Wait For Inspectors 
"""

         ScanButton = [[ InlineKeyboardButton(text="Scan", callback_data="bscan")]]
         await bot.send_message(-1001723857695, text, reply_markup=InlineKeyboardMarkup(ScanButton))
         await msg.edit_text(f"Successfully Scanned [{user_id}](tg://user?id={user_id})")


@bot.on_callback_query(filters.regex("bscan"))
async def bscan(_, query):
       if query.from_user.id in OWO:
           await add_gban_user(user_id)
           await ubot.send_message(-1001781501832, f"/gban {user_id}")
           text = f""" **From Chat:** {query.message.chat.title}
**Enforcer:** [{query.from_user.id}](tg://user?id={query.from_user.id})
**Scanned:** [{user_id}](tg://user?id={user_id})

Aproved by [{query.from_user.id}](tg://user?id={query.from_user.id})"""
           bscan_Button = [[ InlineKeyboardButton(text="revert", callback_data="bunscan")]]
           await query.message.edit(text, reply_markup=InlineKeyboardMarkup(bscan_Button))


@bot.on_callback_query(filters.regex("bunscan"))
async def unscan(_, query):
       if query.from_user.id in OWO:
           await remove_gban_user(user_id)
           await ubot.send_message(-1001781501832, f"/ungban {user_id}")
           text = f""" **From Chat:** {query.message.chat.title}
**Admire:** [{query.from_user.id}](tg://user?id={query.from_user.id})
**UnScanned:** [{user_id}](tg://user?id={user_id})"""
           UnscanButton = [[ InlineKeyboardButton(text="Scan Again", callback_data="bscan")]]
           await query.message.edit(text, reply_markup=InlineKeyboardMarkup(UnscanButton))

