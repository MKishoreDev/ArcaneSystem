from pyrogram import filters
from Arcane import bot
from Arcane.utils.dbfunctions import (
add_enforcers as add_rank, remove_enforcers as add_rank, get_enforcers as get_rankusers)
from Arcane.ranks import Enforcers as RANK_USERS

RANK_ADDED_TEXT = """
new enforcer arrived on bot
it's {}
"""
RANK_REMOVED_TEXT = """
the enforcer remove on bot
it's {}
"""

@bot.on_message(filters.command("addenforcers"))
async def addenforcers(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      msg = await message.reply_text("processing adding..")
      if not message.from_user.id in (await RANK_USERS()):
           await msg.edit_text("my rank user can add another rank user!")
      elif not reply:
         try:
           user_id_text = int(message.text.split(" ")[1])
           user = await bot.get_users(user_id_text)
           if user.id in (await RANK_USERS()):
               await msg.edit("`your trying add someone that person already a rank user`")
           else:
              await add_rank(user.id)
              await msg.edit_text(RANK_ADDED_TEXT.format(user.mention))
         except Exception as e:
             await msg.edit_text(str(e))
         
      else:
            try:
              user_id = reply.from_user.id
              user = await bot.get_users(user_id)
              if user.id in (await RANK_USERS()):
                   await msg.edit("`your trying add someone that person already a rank user`")
              else:
                 await add_rank(user.id)
                 await msg.edit_text(RANK_ADDED_TEXT.format(user.mention))
            except Exception as e:
                  await msg.edit_text(str(e))

@bot.on_message(filters.command("removeenfocers"))
async def removeenforcers(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      msg = await message.reply_text("processing removeing..")
      if not message.from_user.id in (await RANK_USERS()):
           await msg.edit_text("my rank user can remove another rank user!")
      elif not reply:
         try:
           user_id_text = int(message.text.split(" ")[1])
           user = await bot.get_users(user_id_text)
           if not user.id in (await RANK_USERS()):
               await msg.edit("`your trying remove someone that person is not a rank user`")
           else:
              await remove_rank(user.id)
              await msg.edit_text(RANK_REMOVED_TEXT.format(user.mention))
         except Exception as e:
             await msg.edit_text(str(e))
         
      else:
            try:
              user_id = reply.from_user.id
              user = await bot.get_users(user_id)
              if not user.id in (await RANK_USERS()):
                   await msg.edit("`your trying remove someone that person is not a rank user`")
              else:
                 await remove_rank(user.id)
                 await msg.edit_text(RANK_REMOVED_TEXT.format(user.mention))
            except Exception as e:
                  await msg.edit_text(str(e))


@bot.on_message(filters.command("enforcers"))
async def enforcers(_, message):
       chat_id = message.chat.id
       user_id = message.from_user.id
       msg = await message.reply_text("`getting rankusers list!`")
       if not user_id in (await RANK_USERS()):
            await msg.edit_text("`sorry you can't collect rankusers list.`")
       elif user_id in (await RANK_USERS()):
           RANK_USER_TEXT = "𝗥𝗔𝗡𝗞𝗨𝗦𝗘𝗥 𝗟𝗜𝗦𝗧:\n\n"
           try:
              for rankuser in (await get_rankusers()):
                   mention = (await bot.get_users(rankuser)).mention
                   RANK_USER_TEXT += f"• {mention}\n"
                   await msg.edit(RANK_USER_TEXT)
           except Exception as e:
                  await msg.edit(str(e))
