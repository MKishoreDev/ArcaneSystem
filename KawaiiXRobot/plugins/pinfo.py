import asyncio
import random
from KawaiiXRobot import bot, db
from pyrogram import filters
from config import DEVS, Inspector, Enforcer 
from pyrogram.types import Message

SCAN_IMG = (
      "https://telegra.ph/file/9332b113ddb8555bf6ffe.jpg",
      "https://telegra.ph/file/357a3279b2960dd79a549.jpg",
  )

dev_text = f"""
╒═══「 Cringe X System  」
➖➖➖➖➖➖➖➖➖
➣ NAME: {m.from_user.first_name}
➢ RANK: {status}
➖➖➖➖➖➖➖➖➖
╘══「 You are a Kawaii authorized user! 」
"""
buttons = [
    [
        InlineKeyboardButton("📢  Uᴘᴅᴀᴛᴇs", url="https://t.me/playBoysDXD"),
        InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ ⚠️", url="https://t.me/Tamilchat_cringe_guys"),   
    ],
]

@bot.on_message(filters.command("pinfo", ['/', ".", "?"]))
async def status(bot, m: Message):
        await m.reply_photo(
               photo=random.choice(SCAN_IMG),
                caption=dev_text.format(m.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(buttons))

    if m.from_user.id in DEVS:
        status = "**God Of Cringe**"

    elif m.from_user.id in Inspector:
        status = "**Inspector**"

    elif m.from_user.id in Enforcer:
        status = "**Enforcer**"

    elif db.get_role(m.from_user.id)['status'] != True:
        status = "Human"

    elif db.get_role(m.from_user.id)['status'] == True:
        status = db.get_role(m.from_user.id)['role']

    else:
        status = "civilian"

@bot.on_message(filters.command("setrole"))
def setstatus(_, m: Message):
    role = m.text.replace(m.text.split(" ")[0], "")
    if not role == "":
        db.add_role(m.from_user.id, role)
        m.reply("Done!")
    else:
        m.reply("Usage : /setrole role")
