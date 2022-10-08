from pyrogram import filters
from Arcane import bot, DEVS
from Arcane.utils.dbfunctions import (
add_enforcers, remove_enforcers, get_enforcers)
from Arcane.ranks import Enforcers 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Arcane.utils.dbfunctions import (
add_Inspector, remove_Inspector, get_Inspector)
from Arcane.ranks import Inspectors_list

@bot.on_callback_query(filters.regex("addinss"))
async def addinss(_, query):
      if query.from_user.id in DEVS
      await add_Inspector(user_id)
      text = f""" Congratulations [{query.from_user.id}](tg://user?id={query.from_user.id}) Into Inspector"""
      await query.message.edit(text, reply_markup=InlineKeyboardMarkup(PROINS_BUTTON))
