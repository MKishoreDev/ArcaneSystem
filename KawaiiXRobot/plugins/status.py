import asyncio
from KawaiiXRobot import bot, db
from pyrogram import filters
from config import DEVS, Inspector, Enforcer 
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

HMF = DEVS + Inspector + Enforcer 

SCAN_VID = (
      "https://telegra.ph/file/0b2797f78e1756229591a.mp4"
  )

buttons = [
    [
        InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/playBoysDXD"),
        InlineKeyboardButton("Sᴘᴀᴍ ʀᴇᴘᴏʀᴛ", url="https://t.me/playBoysDXD"),   
    ],
]

@bot.on_message(filters.command("status", ['/', ".", "?"]))
async def status(bot, m: Message):
    if m.from_user.id in DEVS:
        status = "**Gᴏᴅ Oғ Cʀɪɴɢᴇ**"

    elif m.from_user.id in Inspector:
        status = "**Iɴsᴘᴇᴄᴛᴏʀ**"

    elif m.from_user.id in Enforcer:
        status = "**Eɴғᴏʀᴄᴇʀ**"

    elif db.get_role(m.from_user.id)['status'] != True:
        status = "Cɪᴠɪʟɪᴀɴ"

    elif db.get_role(m.from_user.id)['status'] == True:
        status = db.get_role(m.from_user.id)['role']

    else:
        status = "Cɪᴠɪʟɪᴀɴ"

    if m.from_user.id in HMF:
        dev_text = f"""
Cʀɪɴɢᴇ Sʏsᴛᴇᴍ

• Nᴀᴍᴇ: {m.from_user.mention}
• Rᴀɴᴋ: {status}

Cʀɪɴɢᴇ Sʏsᴛᴇᴍ Aᴜᴛʜᴏʀɪᴢᴇᴅ
"""
        await m.reply_video(
               SCAN_VID,
                caption=dev_text,              
                reply_markup=InlineKeyboardMarkup(buttons))

    else:
        text = f"""
Cʀɪɴɢᴇ Sʏsᴛᴇᴍ

• Nᴀᴍᴇ: {m.from_user.first_name}
• Rᴀɴᴋ: {status}

Mᴇᴍʙᴇʀ Oғ Cʀɪɴɢᴇ
"""

        await m.reply(text, reply_markup=InlineKeyboardMarkup(buttons))


@bot.on_message(filters.command("setrole"))
def setstatus(_, m: Message):
    role = m.text.replace(m.text.split(" ")[0], "")
    if not role == "":
        db.add_role(m.from_user.id, role)
        m.reply("Done!")
    else:
        m.reply("Usage : /setrole role")
