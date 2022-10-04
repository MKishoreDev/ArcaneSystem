import asyncio 

from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
)
from pyrogram import filters
from Arcane import bot, PREFIX
from Arcane.strings import (START_STRING, HELP_TEXT ANI0, ANI1, ANI2, ANI3, ANI4, ANI5, ANI6, TOXIC_RULES, GROUP_RULES, G_B_RULES, INSPECTOR_RULES, RULES_TEXT, BANCODES)
from Arcane.media import ANIMATION_MEDIA, START_MEDIA, HELP_MEDIA, RULES_MEDIA
from Arcane.buttons import START_BUTTON, HELP_BUTTON, SCANHELP_BUTTON, SCANHELP_BUTTON2, SCANHELP_BUTTON3, RULES_BUTTON, RULES_BUTTON2

@bot.on_message(filters.command(["start"], PREFIX))
async def start(_, m: Message):
    kk = await m.reply_photo(ANIMATION_MEDIA, caption=ANI0)
    await asyncio.sleep(2)
    await kk.edit_caption(ANI1)
    await asyncio.sleep(2)
    await kk.edit_caption(ANI2)
    await asyncio.sleep(2)
    await kk.edit_caption(ANI3)
    await asyncio.sleep(2)
    await kk.edit_caption(ANI4)
    await asyncio.sleep(2)
    await kk.edit_caption(ANI5)
    await asyncio.sleep(2)
    await kk.edit_caption(ANI6)
    await asyncio.sleep(1)
    await kk.delete()     
    await m.reply_video(
        START_MEDIA,
        caption=START_STRING.format(
            m.from_user.mention
        ),
        reply_markup=InlineKeyboardMarkup(START_BUTTON),
    )

@bot.on_message(filters.command("help", COMMANDS))
async def help(client, message):
    await message.reply_video(HELP_MEDIA, caption=HELP_TEXT,
                              reply_markup=InlineKeyboardMarkup(HELP_BUTTON))

@bot.on_callback_query(filters.regex("scan_help"))
async def scanhelp(_, query: CallbackQuery):
    await query.edit_message_caption("""How to scan 

👉🏻 1st case if scanning the user via replying to that user message,
Use command /scan + flags checkout flags button.

`E.g /scan -r threat -p https://telegra.ph/media`

👉🏻 2nd case if scanning the user via "message link/username/user id"
Use command /scan -id + flags checkout flags button.

`E.g /scan -id 1234560914 -r threat -p https://telegra.ph/media`""",
       reply_markup=InlineKeyboardMarkup(SCANHELP_BUTTON))
        
@bot.on_callback_query(filters.regex("bancodes_help"))
async def bancodes(_, query: CallbackQuery):
    await query.edit_message_caption(BANCODES,
       reply_markup=InlineKeyboardMarkup(SCANHELP_BUTTON))

@bot.on_callback_query(filters.regex("back_help"))
async def helpback(_, query: CallbackQuery):
    await query.edit_message_caption(HELP_TEXT,
       reply_markup=InlineKeyboardMarkup(SCANHELP_BUTTON2))
    
@bot.on_callback_query(filters.regex("back_start"))
async def startback(_, query: CallbackQuery):
    await query.edit_message_caption(START_STRING.format(m.from_user.mention),
       reply_markup=InlineKeyboardMarkup(SCANHELP_BUTTON3))

@bot.on_callback_query(filters.regex("delete"))
async def delete(_, query):
    await query.message.delete()

@bot.on_message(filters.command("rules", PREFIX))
async def rules(client, message):
    await message.reply_video(RULES_MEDIA, caption=RULES_TEXT,
                              reply_markup=InlineKeyboardMarkup(RULES_BUTTON))

@bot.on_callback_query(filters.regex("Rules"))
async def rules(_, query: CallbackQuery):
    await query.edit_message_caption(RULES_TEXT,
        reply_markup=InlineKeyboardMarkup(RULES_BUTTON2))
        
@bot.on_callback_query(filters.regex("basic_scanner_rules"))
async def basichelp(_, query: CallbackQuery):
    await query.edit_message_caption(INSPECTOR_RULES,
        reply_markup=InlineKeyboardMarkup(RULES_BUTTON2))
        
@bot.on_callback_query(filters.regex("Girls_Safe_Rule"))
async def girlssafe(_, query: CallbackQuery):
    await query.edit_message_caption(G_B_RULES,
        reply_markup=InlineKeyboardMarkup(RULES_BUTTON2))
        

@bot.on_callback_query(filters.regex("group_rules"))
async def basicgrouprules(_, query: CallbackQuery):
    await query.edit_message_caption(GROUP_RULES,
        reply_markup=InlineKeyboardMarkup(RULES_BUTTON2))
        

@bot.on_callback_query(filters.regex("Toxic_Boom"))
async def basictoxirules(_, query: CallbackQuery):
    await query.edit_message_caption(TOXIC_RULES,
        reply_markup=InlineKeyboardMarkup(RULES_BUTTON2))

        
