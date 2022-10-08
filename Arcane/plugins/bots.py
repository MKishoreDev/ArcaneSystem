import time
import pytz
import datetime
from Arcane import bot, DEVS, Inspector, Enforcer, ubot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
from pyrogram.types import Message
from Arcane.utils.db_botlist import (
    add_bots_user, remove_bots_user
)

from Arcane.utils.db_botlist import botsdb
from Arcane.utils import db_botlist as x

OWO = DEVS
COMMANDS = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]

india_Date_Time = datetime.datetime.now(tz=pytz.timezone("Asia/Calcutta"))
Current_Date_Time = india_Date_Time.strftime("%Y-%m-%dT%H:%M")

@bot.on_message(filters.command("addbot", COMMANDS))
async def scanning(_, message):
         global user_id
         if message.from_user.id not in OWO:
              return await message.reply_text("Sorry You Can't Add Bots 😑") 
         if len(message.command) <2:
                  await message.reply("* Add Current Status Of That Bot")
                  return 
         elif message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                admire = message.from_user.id
                reason = message.text.replace("/addbot", "")
                       
         msg = await message.reply_text("**Bot Connecting to Arcane System...**")
         await add_bots_user(user_id)
         text = f""" **From Chat:** {message.chat.title}
**Developer:** [{admire}](tg://user?id={admire})
**Bot:** [{user_id}](tg://user?id={user_id})
**Bot Status**: {reason}
**Event Stamp:** {Current_Date_Time}
"""

         await bot.send_message(-1001723857695, text)
         await msg.edit_text(f"Successfully Bot Added [{user_id}](tg://user?id={user_id})")


@bot.on_message(filters.command("rmbot"))
async def revive(_, message):
          
          if message.from_user.id in OWO and message.reply_to_message:
                       await x.remove_bots_user(message.reply_to_message.from_user.id)
                       await message.reply(f"Arcane Dev: {message.from_user.id}\n target Bot: {message.reply_to_message.from_user.id}\n **Bot Removed**")  
          
          else:
                if message.from_user.id not in OWO:
                      return await message("Only Arcane Dev can use")
                elif len(message.command) <2:
                      return await message.reply("give a user ID or name")
                elif not message.reply_to_message:
                     user_id_text = message.text.split(None, 1)[1]
                     user = await bot.get_users(user_id_text)
                     await x.remove_bots_user(user.id)
                     await message.reply(f"Arcane User: {message.from_user.id}\n target user: {user.id}\n **Bot Removed**")
             
@bot.on_message(filters.command("bots", COMMANDS))
async def list(client, message):
   total_num = len([i async for i in botsdb.find({"user_id": {"$gt": 0}})])
   total_id = ([i['user_id'] async for i in botsdb.find({"user_id": {"$gt": 0}})])
   reply = f"`{total_num}` **Under Arcane Bots\n**"
   for x in total_id:
       user = await bot.get_users(int(x))
       mention = "[" + user.first_name + "](tg://user?id=" + str(user.id) + ")" or user.first_name
       reply += f"• {mention}\n"     
   try: 
      await message.reply_video("https://telegra.ph/file/65239f3043ca5161617df.mp4", caption=reply)      
   except Exception as e:
       print(e)
   if len(reply.split("\n")) < 2:
       return await message.reply_text("No Bots Added.")

