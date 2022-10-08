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
async def addinss(_, query):
       if query.from_user.id in DEVS:
               await add_Inspector(user_id)
               ADDIND_TEXT = f"""[{query.from_user.id}](tg://user?id={query.from_user.id}) Promoted [{user_id}](tg://user?id={user_id}) Into Inspector"""
               await query.edit_message_caption(ADDIND_TEXT, reply_markup=InlineKeyboardMarkup(INSED_BUTTON))

@bot.on_callback_query(filters.regex("ADDENF"))
async def addenfs(_, query):
       if query.from_user.id in DEVS:
               await add_enforcers(user_id)
               ADDENF_TEXT = f"""[{query.from_user.id}](tg://user?id={query.from_user.id}) Successful Promoted [{user_id}](tg://user?id={user_id}) Into Enforcer"""
               await query.edit_message_caption(ADDENF_TEXT, reply_markup=InlineKeyboardMarkup(ENFED_BUTTON))

@bot.on_callback_query(filters.regex("RMINS"))
async def rmins(_, query):
       if query.from_user.id in DEVS:
               await remove_Inspector(user_id)
               RMINS_TEXT = f"""[{query.from_user.id}](tg://user?id={query.from_user.id}) Successfully [{user_id}](tg://user?id={user_id}) Into civilian"""
               await query.edit_message_caption(RMINS_TEXT, reply_markup=InlineKeyboardMarkup(CIVED_BUTTON))

@bot.on_callback_query(filters.regex("RMENF"))
async def rmenf(_, query):
       if query.from_user.id in DEVS:
               await remove_enforcers(user_id)
               RMINS_TEXT = f"""[{query.from_user.id}](tg://user?id={query.from_user.id}) Successfully [{user_id}](tg://user?id={user_id}) Into civilian"""
               await query.edit_message_caption(RMINS_TEXT, reply_markup=InlineKeyboardMarkup(CIVED_BUTTON))

@bot.on_callback_query(filters.regex("delete"))
async def delete(_, query):
    await query.message.delete()
