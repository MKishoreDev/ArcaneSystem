import time
import pytz
import datetime
from KawaiiXRobot import bot, KAWAII_LOGS, DEVS, Inspector, Enforcer, KAWAII_CHANNEL, ubot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
from pyrogram.types import Message
from KawaiiXRobot.utils.db_ins import (
    add_Inspector_user, remove_Inspector_user
)

from KawaiiXRobot.utils.db_ins import Inspectordb
from KawaiiXRobot.utils import db_ins as x

OWO = DEVS
COMMANDS = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]

india_Date_Time = datetime.datetime.now(tz=pytz.timezone("Asia/Calcutta"))
Current_Date_Time = india_Date_Time.strftime("%Y-%m-%dT%H:%M")

@bot.on_message(filters.command("add", COMMANDS))
async def scanning(_, message):
         global user_id
         if message.from_user.id not in OWO:
              return await message.reply_text("You Don't Have Rights To Add 😑") 
         if len(message.command) <2:
                  await message.reply("* Reason For Adding For Inspector ")
                  return 
         elif message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                admire = message.from_user.id
                reason = message.text.replace("/add", "")
                       
         msg = await message.reply_text("**Connecting to Cringe System...**")
         await add_Inspector_user(user_id)
         text = f""" **From Chat:** {message.chat.title}
**Developer:** [{admire}](tg://user?id={admire})
**New Inspector:** [{user_id}](tg://user?id={user_id})
**Information**: {reason}
**Event Stamp:** {Current_Date_Time}
"""

         await bot.send_message(-1001723857695, text)
         await msg.edit_text(f"Successfully Inspector Added [{user_id}](tg://user?id={user_id})")


@bot.on_message(filters.command("rmins"))
async def revive(_, message):
          
          if message.from_user.id in OWO and message.reply_to_message:
                       await x.remove_Inspector_user(message.reply_to_message.from_user.id)
                       await message.reply(f"Cringe Dev: {message.from_user.id}\n X-Ins: {message.reply_to_message.from_user.id}\n **Demoted Done 👍**")  
          
          else:
                if message.from_user.id not in OWO:
                      return await message("Only Cringe Dev can use")
                elif len(message.command) <2:
                      return await message.reply("give a user ID or name")
                elif not message.reply_to_message:
                     user_id_text = message.text.split(None, 1)[1]
                     user = await bot.get_users(user_id_text)
                     await x.remove_Inspector_user(user.id)
                     await message.reply(f"Cringe User: {message.from_user.id}\n target user: {user.id}\n **Bot Removed**")
             
@bot.on_message(filters.command("Inspectors", COMMANDS))
async def list(client, message):
   total_num = len([i async for i in Inspectordb.find({"user_id": {"$gt": 0}})])
   total_id = ([i['user_id'] async for i in Inspectordb.find({"user_id": {"$gt": 0}})])
   reply = f"`{total_num}` ** Cringe Inspectors List\n**"
   for x in total_id:
       user = await bot.get_users(int(x))
       mention = "[" + user.first_name + "](tg://user?id=" + str(user.id) + ")" or user.first_name
       reply += f"• {mention}\n"     
   try: 
      await message.reply_video("https://telegra.ph/file/65239f3043ca5161617df.mp4", caption=reply)      
   except Exception as e:
       print(e)
   if len(reply.split("\n")) < 2:
       return await message.reply_text("No one Added.")
