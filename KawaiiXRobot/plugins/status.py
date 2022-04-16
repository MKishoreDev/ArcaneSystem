import asyncio
import time

from Cringe import bot, db, DEVS, CRINGE_GUYS, CRINGE_KID
from pyrogram import filters
from pyrogram.types import Message

on_string = """
╒═══「 Cringe X System • Server Core 」
➖➖➖➖➖➖➖➖➖
➣ NAME: {name}
➢ RANK: {status}
➖➖➖➖➖➖➖➖➖
╘══「 You are a Cringe authorized user! 」
"""

CIRINGE = "https://telegra.ph/file/c5a59655aede70ac6135c.mp4"
@bot.on_message(filters.command("status", ['/', ".", "?"]))
async def status(bot, m: Message):
    msg = await m.reply("Conecting to Cringe X System System Core.")
    time.sleep(1)
    await msg.edit("Initialising ✦✧✧✧✧✧")
    time.sleep(1)
    await msg.edit("Initialising ✦✦✧✧✧✧")
    time.sleep(1)
    await msg.edit("Initialising ✦✦✦✧✧✧")
    time.sleep(1)
    await msg.edit("Initialising ✦✦✦✦✧✧")
    time.sleep(1)
    await msg.edit("Initialising ✦✦✦✦✦✧")
    time.sleep(1)
    await msg.edit("Initialising ✦✦✦✦✦✦")
    time.sleep(1)
    await msg.edit("✪VᴇRɪFɪᴇD✪")
    time.sleep(2)
    if m.from_user.id in DEVS:
        status = "**God Of Cringe**"

    if m.from_user.id in CRINGE_GUYS:
        status = "**Guys Of Cringe**"

    if m.from_user.id in CRINGE_KID:
        status = "**Kid Of Cringe**"

    elif db.get_role(m.from_user.id)['status'] != True:
        status = "Human Of Cringe"

    elif db.get_role(m.from_user.id)['status'] == True:
        status = db.get_role(m.from_user.id)['role']

    else:
        status = "Human"
    time.sleep(1)
    await msg.edit(on_string.format(status=status, name=m.from_user.mention, file=CIRINGE))

@bot.on_message(filters.command("cringe"))
def setstatus(_, m: Message):
    role = m.text.replace(m.text.split(" ")[0], "")
    if role != "":
        db.add_role(m.from_user.id, role)
        m.reply("`Done!`")
    else:
        m.reply("Usage : `/cringe cringe role`")
