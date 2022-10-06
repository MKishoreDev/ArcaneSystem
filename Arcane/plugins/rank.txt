from Arcane import Enforcer 
from Arcane.utils.addenf_db import (
get_enfusers, add_enf, remove_enf)
enf_ADDED_TEXT = """
new enf user arrived on bot
it's {}
"""
enf_REMOVED_TEXT = """
the enf user remove on bot
it's {}
"""
@bot.on_message(filters.command("addenf"))
async def addenf(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      msg = await message.reply_text("processing adding..")
      if not message.from_user.id in (await Enforcer()):
           await msg.edit_text("my enf user can add another enf user!")
      elif not reply:
         try:
           user_id_text = int(message.text.split(" ")[1])
           user = await bot.get_users(user_id_text)
           if user.id in (await Enforcer()):
               await msg.edit("`your trying add someone that person already a enf user`")
           else:
              await add_enf(user.id)
              await msg.edit_text(enf_ADDED_TEXT.format(user.mention))
         except Exception as e:
             await msg.edit_text(str(e))
         
      else:
            try:
              user_id = reply.from_user.id
              user = await bot.get_users(user_id)
              if user.id in (await Enforcer()):
                   await msg.edit("`your trying add someone that person already a enf user`")
              else:
                 await add_enf(user.id)
                 await msg.edit_text(enf_ADDED_TEXT.format(user.mention))
            except Exception as e:
                  await msg.edit_text(str(e))
@bot.on_message(filters.command("rmenf"))
async def removeenf(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      msg = await message.reply_text("processing removeing..")
      if not message.from_user.id in (await Enforcer()):
           await msg.edit_text("my enf user can remove another enf user!")
      elif not reply:
         try:
           user_id_text = int(message.text.split(" ")[1])
           user = await bot.get_users(user_id_text)
           if not user.id in (await Enforcer()):
               await msg.edit("`your trying remove someone that person is not a enf user`")
           else:
              await remove_enf(user.id)
              await msg.edit_text(enf_REMOVED_TEXT.format(user.mention))
         except Exception as e:
             await msg.edit_text(str(e))
         
      else:
            try:
              user_id = reply.from_user.id
              user = await bot.get_users(user_id)
              if not user.id in (await Enforcer()):
                   await msg.edit("`your trying remove someone that person is not a enf user`")
              else:
                 await remove_enf(user.id)
                 await msg.edit_text(enf_REMOVED_TEXT.format(user.mention))
            except Exception as e:
                  await msg.edit_text(str(e))
@bot.on_message(filters.command("enfusers"))
async def enfuser(_, message):
       chat_id = message.chat.id
       user_id = message.from_user.id
       msg = await message.reply_text("`getting enfusers list!`")
       if not user_id in (await Enforcer()):
            await msg.edit_text("`sorry you can't collect enfusers list.`")
       elif user_id in (await Enforcer()):
           enf_USER_TEXT = "𝗥𝗔𝗡𝗞𝗨𝗦𝗘𝗥 𝗟𝗜𝗦𝗧:\n\n"
           try:
              for enfuser in (await get_enfusers()):
                   mention = (await bot.get_users(enfuser)).mention
                   enf_USER_TEXT += f"• {mention}\n"
                   await msg.edit(enf_USER_TEXT)
           except Exception as e:
                  await msg.edit(str(e))
