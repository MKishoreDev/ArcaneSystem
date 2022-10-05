# status.py ©Copyright By @HMF_Owner_1 

import asyncio
from Arcane import bot, db
from Arcane.media import *
from Arcane.buttons import *
from pyrogram import filters
from config import DEVS, Inspector, Enforcer, PREFIX
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

HMF = DEVS + Inspector + Enforcer 

@bot.on_message(filters.command("status", PREFIX))
async def status(bot, m: Message):
    if m.from_user.id in DEVS:
        status = "**Developer**"

    elif m.from_user.id in Inspector:
        status = "**Inspector**"

    elif m.from_user.id in Enforcer:
        status = "`Enforcer`"
    else:
        status = "Civilian"

    if m.from_user.id in HMF:
        dev_text = f"""
Aʀᴄᴀɴᴇ Sʏsᴛᴇᴍ

• Nᴀᴍᴇ: {m.from_user.mention}
• Rᴀɴᴋ: {status}

Aʀᴄᴀɴᴇ Sʏsᴛᴇᴍ Aᴜᴛʜᴏʀɪᴢᴇᴅ
"""
        await m.reply_video(
               STATUS_MEDIA,
                caption=dev_text,              
                reply_markup=InlineKeyboardMarkup(STATUS_BUTTON))

    else:
        text = f"""
Aʀᴄᴀɴᴇ Sʏsᴛᴇᴍ

• Nᴀᴍᴇ: {m.from_user.first_name}
• Rᴀɴᴋ: {status}

Mᴇᴍʙᴇʀ Oғ Cʀɪɴɢᴇ
"""

        await m.reply(text, reply_markup=InlineKeyboardMarkup(buttons))


# @bot.on_message(filters.command("setrole", PREFIX))
# def setstatus(_, m: Message):
    # role = m.text.replace(m.text.split(" ")[0], "")
    # if not role == "":
        # db.add_role(m.from_user.id, role)
        # m.reply("Dᴏɴᴇ!")
    # else:
        # m.reply("Usᴀɢᴇ : /setrole ʀᴏʟᴇ")
