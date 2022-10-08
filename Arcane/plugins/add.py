from pyrogram import filters
from Arcane.strings import *
from Arcane.media import *
from Arcane.buttons import *
from Arcane import bot, DEVS, PREFIX
from Arcane.utils.dbfunctions import (
add_enforcers, remove_enforcers, get_enforcers)
from Arcane.utils.dbfunctions import (
add_Inspector, remove_Inspector, get_Inspector)
from Arcane.ranks import Enforcers 
from Arcane.ranks import Inspectors_list
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

@bot.on_message(filters.command("add", PREFIX))
async def start(_, m: Message):
         global user_id
         if m.from_user.id not in DEVS:
              return await message.reply_text("WTF! You'er My Developer") 
         if m.reply_to_message:
                user_id = m.reply_to_message.from_user.id
                admin = m.from_user.id
                await m.reply_photo(ADD_MEDIA,
                caption=ADD_STRIMG.format(
                m.from_user.mention
               ),
              reply_markup=InlineKeyboardMarkup(ADD_BUTTON),
           )

@bot.on_callback_query(filters.regex("ADDINS"))
async def addinss(_, query: CallbackQuery):
       user_id = message.reply_to_message.from_user.id
       admin = message.from_user.id
       if query.from_user.id in DEVS:
               await add_Inspector(user_id)
               ADDIND_TEXT = f"""  [{admin}](tg://user?id={admin}) Promoted [{query.from_user.id}](tg://user?id={query.from_user.id}) Into Inspector"""
               await query.edit_message_caption(ADDIND_TEXT, reply_markup=InlineKeyboardMarkup(INSED_BUTTON))


