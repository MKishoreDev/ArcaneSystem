# Sacnlist.py ©Copyright By @ProErrorDxD Machan

from pyrogram import filters, Client
from KawaiiXRobot import bot
from KawaiiXRobot.utils.dbfunctions import gbansdb

@bot.on_message(filters.command(["scanlist"], ['/', ".", "?"]))
async def list(client, message):
   total_num = len([i async for i in gbansdb.find({"user_id": {"$gt": 0}})])
   total_id = ([i['user_id'] async for i in gbansdb.find({"user_id": {"$gt": 0}})])
   reply = f"`{total_num}` **Globally Scanned/Banned Users\n**"
   for x in total_id:
       user = await bot.get_users(int(x))
       mention = "[" + user.first_name + "](tg://user?id=" + str(user.id) + ")" or user.first_name
       reply += f"• {mention}\n"     
   try: 
      await message.reply_video("https://telegra.ph/file/65239f3043ca5161617df.mp4", caption=reply)      
   except Exception as e:
       print(e)
   if len(reply.split("\n")) < 2:
       return await message.reply_text("No Scanned/Banned Found.")
