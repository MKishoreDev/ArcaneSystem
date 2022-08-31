from pyrogram import filters, Client
from KawaiiXRobot import bot
from KawaiiXRobot.utils.dbfunctions import gbansdb

@bot.on_message(filters.command(["scanlist"], ['/', ".", "?"]))
async def list(client, message):
   total_num = len([i async for i in gbansdb.find({"user_id": {"$gt": 0}})])
   total_id = ([i['user_id'] async for i in gbansdb.find({"user_id": {"$gt": 0}})])
   for x in total_id:
       try: 
           user = await bot.get_users(x)
           mention = "[" + user.first_name + "](tg://user?id=" + str(user.id) + ")"
           reply = "`{}` **Globally Scanned/Banned Users**".format(total_num)
           reply += "• {}\n".format(mention)
           hehe = "https://telegra.ph/file/65239f3043ca5161617df.mp4"
           await message.reply_video(hehe, caption=reply)
       except Exception as e:
           print(e)
