import asyncio
from KawaiiXRobot import bot, db
from pyrogram import filters
from config import DEVS, Inspector, Enforcer 
from pyrogram.types import Message

@bot.on_message(filters.command("pinfo", ['/', ".", "?"]))
async def status(bot, m: Message):

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


        await m.reply_photo("https://telegra.ph/file/ddd825c338fa668a4252d.jpg",
                caption=dev_text.format(m.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(buttons))


@bot.on_message(filters.command("setrole"))
def setstatus(_, m: Message):
    role = m.text.replace(m.text.split(" ")[0], "")
    if not role == "":
        db.add_role(m.from_user.id, role)
        m.reply("Done!")
    else:
        m.reply("Usage : /setrole role")
