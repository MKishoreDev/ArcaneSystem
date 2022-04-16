from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from KawaiiXRobot import bot

Kawaii = """
<b>Hey</b> {} <b>Welcome To Kawaii X Robot</b> 
<b>An Advanced System To Make Telegram Safe</b>
<b>Checkout The</b> `/help`
"""
hehe = "https://telegra.ph/file/39daf97898a10f039e6b3.jpg"

@bot.on_message(filters.command(["start"], ['/', ".", "?"]))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton("Support", url="https://t.me/PlayBoysDXD"),
    ]]
    await message.reply_video(hehe, caption=Kawaii.format(message.from_user.mention),
                             reply_markup=InlineKeyboardMarkup(buttons))

@bot.on_message(filters.command(["help"], ['/', ".", "?"]))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton("Dev", url="https://t.me/HMF_OWNER_1"),
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

**Clan Of Kawaii X System Commands** :

/scan userid reason or reply to user - Ban User
/unscan userid - Unban User
/gscan Username - All Group Admin Ban
/ungscan Username - All Group Admin Unban
/logs - Check Kawaii X system logs""",
                             reply_markup=InlineKeyboardMarkup(buttons))
