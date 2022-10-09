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
from Arcane.plugins.info import *
from Arcane.ranks import Inspectors_list
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

@bot.on_message(filters.command("add", PREFIX))
async def info_func(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("Processing")

    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await bot.download_media(photo_id)

    await message.reply_photo(photo, caption=info_caption, quote=False, reply_markup=InlineKeyboardMarkup(ADD_BUTTON),
           )

@bot.on_callback_query(filters.regex("I_TO_E"))
async def ITE(_, query):
       if query.from_user.id in DEVS:
               await remove_Inspector(user_id)
               await add_enforcers(user_id)
               I_TO_E_TEXT = f"""Successfully Inspector [{user_id}](tg://user?id={user_id}) Demoted Into Enforcer"""
               await query.edit_message_caption(I_TO_E_TEXT, reply_markup=InlineKeyboardMarkup(I_TO_E_BUTTON))

@bot.on_callback_query(filters.regex("E_TO_I"))
async def ETI(_, query):
       if query.from_user.id in DEVS:
               await remove_enforcers(user_id)
               await add_Inspector(user_id)
               E_TO_I_TEXT = f"""Successfully Enforcer [{user_id}](tg://user?id={user_id}) Promoted Into Inspector"""
               await query.edit_message_caption(E_TO_I_TEXT, reply_markup=InlineKeyboardMarkup(E_TO_I_BUTTON))

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
               await query.edit_message_caption(RMINS_TEXT, reply_markup=InlineKeyboardMarkup(RMINSED_BUTTON))

@bot.on_callback_query(filters.regex("RMENF"))
async def rmenf(_, query):
       if query.from_user.id in DEVS:
               await remove_enforcers(user_id)
               RMENF_TEXT = f"""[{query.from_user.id}](tg://user?id={query.from_user.id}) Successfully [{user_id}](tg://user?id={user_id}) Into civilian"""
               await query.edit_message_caption(RMENF_TEXT, reply_markup=InlineKeyboardMarkup(RMENFED_BUTTON))

@bot.on_callback_query(filters.regex("EXTRA_DEMOTEE"))
async def rmenf(_, query):
       if query.from_user.id in DEVS:
               EXTRA_TEXT = f"""Welcome To Arcane System"""
               await query.edit_message_caption(EXTRA_TEXT, reply_markup=InlineKeyboardMarkup(EXTRA_DEMOTE))

@bot.on_callback_query(filters.regex("ADDD_BUTTON"))
async def rmenf(_, query):
       if query.from_user.id in DEVS:
               LOW_TEXT = f"""Welcome To Arcane System"""
               await query.edit_message_caption(LOW_TEXT, reply_markup=InlineKeyboardMarkup(ADD_BUTTON))

@bot.on_callback_query(filters.regex("deletee"))
async def delete(_, query):
       if query.from_user.id in DEVS:
               await query.message.delete()
