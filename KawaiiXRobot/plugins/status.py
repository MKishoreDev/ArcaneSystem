import asyncio
import time

from KawaiiXRobot import bot, db
from pyrogram import filters
from config import DEVS, Inspector, Enforcer 
from pyrogram.types import Message

on_string = """
╒═══「 Kawaii X System • Server Core 」
➖➖➖➖➖➖➖➖➖
➣ NAME: {name}
➢ RANK: {status}
➖➖➖➖➖➖➖➖➖
╘══「 You are a Kawaii authorized user! 」
"""

KAWAII = "https://telegra.ph/file/c5a59655aede70ac6135c.mp4"
@bot.on_message(filters.command("status", ['/', ".", "?"]))
async def status(bot, m: Message):
    msg = await m.reply("Conecting to Kawaii X System System Core.")
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
        status = "**DEV - Inspector**"

    if m.from_user.id in Inspector:
        status = "**Inspector**"

    if m.from_user.id in Enforcer:
        status = "**Enforcer**"

    elif db.get_role(m.from_user.id)['status'] == True:
        status = db.get_role(m.from_user.id)['role']

    else:
        status = "Human of Cringe"
    time.sleep(1)
    await msg.edit(on_string.format(status=status, name=m.from_user.mention, file=KAWAII))

@bot.on_message(filters.command("Kawaii"))
def setstatus(_, m: Message):
    role = m.text.replace(m.text.split(" ")[0], "")
    if role != "":
        db.add_role(m.from_user.id, role)
        m.reply("`Done!`")
    else:
        m.reply("Usage : `/Kawaii role`")
