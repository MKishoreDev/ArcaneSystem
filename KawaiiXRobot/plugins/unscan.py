# unacn.py ©Copyright By @NandhaXD Machan

import time
import pytz
import datetime
from KawaiiXRobot import bot, KAWAII_LOGS, DEVS, Inspector, KAWAII_CHANNEL, Enforcer
from pyrogram import filters
from pyrogram import Client
import time
from pyrogram.types import Message
from KawaiiXRobot.utils.dbfunctions import (
    add_gban_user,
    remove_gban_user,
)
from KawaiiXRobot.utils import dbfunctions as x

COMMANDS = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]

OWO = DEVS + Inspector

india_Date_Time = datetime.datetime.now(tz=pytz.timezone("Asia/Calcutta"))
Current_Date_Time = india_Date_Time.strftime("%Y-%m-%dT%H:%M")

@bot.on_message(filters.command("revert", COMMANDS))
async def revert(_, message):
         global user_id
         if message.from_user.id not in OWO:
              return await message.reply_text("Sorry bitch your not my own user") 
         elif message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                admire = message.from_user.id

         if int(user_id) in DEVS:
             await message.reply_text(
                 "Dev's Can't Be UnBan😑"
             )
             return

         if int(user_id) in Inspector:
             await message.reply_text(
                 "Inspector's Can't Be UnBan 😑"
             )
             return

         if int(user_id) in Enforcer:
             await message.reply_text(
                 "Enforcer's Can't Be UnBan 😑. If You Want Ban Or Remove Enforcer Ask Dev With Correct Reason 👍"
             )
             return
                       
         msg = await message.reply_text("**Connecting to Cringe System...**")
         await remove_gban_user(user_id)
         Untext = f"""**From Chat:** {message.chat.title}
**Admire:** [{admire}](tg://user?id={admire})
**UnScanned:** [{user_id}](tg://user?id={user_id})
**Event Stamp:** {Current_Date_Time}
"""

         await ubot.send_message(-1001781501832, f"/ugban {user_id}")
         await bot.send_message(-1001723857695, Untext)
         await msg.edit_text(f"Successfully UnScanned [{user_id}](tg://user?id={user_id})")

# Testing 
@bot.on_message(filters.command("boom"))
async def revive(_, message):

          if message.from_user.id in OWO and message.reply_to_message:
                       await x.remove_gban_user(message.reply_to_message.from_user.id)
                       await message.reply(f"Kawai User: {message.from_user.id}\n target user: {message.reply_to_message.from_user.id}\n **UNBANNED**")  

          else:
                if message.from_user.id not in OWO:
                      return await message("Only OWO user can use")
                elif len(message.command) <2:
                      return await message.reply("give a user ID or name")
                elif not message.reply_to_message:
                     user_id_text = message.text.split(None, 1)[1]
                     user = await bot.get_users(user_id_text)
                     await x.remove_gban_user(user.id)
                     await message.reply(f"Kawai User: {message.from_user.id}\n target user: {user.id}\n **UNBANNED**")

