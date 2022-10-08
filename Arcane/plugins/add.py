from pyrogram import filters
from Arcane import bot, DEVS, PREFIX
from Arcane.utils.dbfunctions import (
add_enforcers, remove_enforcers, get_enforcers)
from Arcane.ranks import Enforcers 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Arcane.utils.dbfunctions import (
add_Inspector, remove_Inspector, get_Inspector)
from Arcane.ranks import Inspectors_list

@bot.on_message(filters.command("add", PREFIX))
async def start(_, m: Message):
         global user_id
         if message.from_user.id not in DEVS:
              return await message.reply_text("WTF! You'er My Developer") 
         if message.reply_to_message:
                await m.reply_video(ADD_MEDIA,
                caption=ADD_STRIMG.format(
                m.from_user.mention
               ),
              reply_markup=InlineKeyboardMarkup(ADD_BUTTON),
           )

@bot.on_callback_query(filters.regex("ADDINS"))
async def addinss(_, query):
       user_id = message.reply_to_message.from_user.id
       admin = message.from_user.id
       if query.from_user.id in DEVS:
               await add_Inspector(user_id)
               text = f"""  [{admin}](tg://user?id={admin}) Promoted [{query.from_user.id}](tg://user?id={query.from_user.id}) Into Inspector"""
               await query.message.edit(text, reply_markup=InlineKeyboardMarkup(PROINS_BUTTON))
