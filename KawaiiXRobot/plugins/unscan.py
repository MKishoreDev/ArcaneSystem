# unacn.py ©Copyright By @NandhaXD Machan

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

@bot.on_message(filters.command("revert", COMMANDS))
async def revert(_, message):
         global user_id
         if message.from_user.id not in OWO:
              return await message.reply_text("Sorry bitch your not my own user") 
         if len(message.command) <2:
                  await message.reply("*Any reason to Unscan ?")
                  return 
         elif message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                admire = message.from_user.id
                reason = message.text.replace("/revert", "")

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
         await x.remove_gban_user(user_id)
         text = f"""#UnScanned

**From Chat:** {message.chat.title}
**Admire:** [{admire}](tg://user?id={admire})
**UnScanned:** [{user_id}](tg://user?id={user_id})
**Reason**: {reason}
**Event Stamp:** {Current_Date_Time}
"""

         await ubot.send_message(-1001781501832, f"/ugban {user_id} {reason}")
         await bot.send_message(-1001723857695, text)
         await msg.edit_text(f"Successfully Scanned [{user_id}](tg://user?id={user_id})")

