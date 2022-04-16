from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Cringe import bot

cringeguys = """
<b>Hey</b> {} <b>Welcome To CringeXSystem</b> 
<b>An Advanced System To Make Telegram Safe</b>
<b>Checkout The</b> `/help`
"""
hehe = "https://telegra.ph/file/51f6b8109b0731db41394.mp4"

@bot.on_message(filters.command(["start"], ['/', ".", "?"]))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton("Dev", url="https://t.me/Aasf_Cyberking"),
    ]]
    await message.reply_video(hehe, caption=cringeguys.format(message.from_user.mention),
                             reply_markup=InlineKeyboardMarkup(buttons))

@bot.on_message(filters.command(["help"], ['/', ".", "?"]))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton("Dev", url="https://t.me/Aasf_Cyberking"),
    ]]
    await message.reply_text(""" **COMMANDS** :  

**Human Commands** :

/start - Start Mesasage
/help - Help Message
/ping - To  check ping
/info - Check your info you scan or not
/ginfo - Group info
/status - Status Check your level
/check userid or reply to user - Check User
/setrole - Roles Name
/report - Report Message

**Clan Of Cringe X System Commands** :

/scan userid reason or reply to user - Ban User
/unscan userid - Unban User
/gscan Username - All Group Admin Ban
/ungscan Username - All Group Admin Unban
/logs - Check Cringe X system logs""",
                             reply_markup=InlineKeyboardMarkup(buttons))
