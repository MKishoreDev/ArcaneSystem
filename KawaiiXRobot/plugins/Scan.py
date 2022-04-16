from Cringe import bot, CRINGE_LOGS, DEVS, CRINGE_GUYS, CRINGE_CHANNEL
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
import time
from pyrogram.types import Message
from Cringe.utils.dbfunctions import (
    add_gban_user,
)

OWO = DEVS + CRINGE_GUYS

@bot.on_message(filters.command("scan", prefixes=["/", ".", "?", "-"]))
async def ban(Client, m: Message):
    if not m.from_user.id in OWO:
        await m.reply_text("Only The Cringe Heros Can Use Me")

    if m.from_user.id in OWO and not m.reply_to_message:
        user = m.command[1]
        reason = m.text.replace(m.text.split(" ")[0], "").replace(user, "")
        enforcer = m.from_user.id

        if len(user) != 10:
            await m.reply_text("Invalid id")
            return

        if not user.isdigit():
            await m.reply_text("User ID Must Be Integer")
            return

        else:
            await add_gban_user(user)
            if user not in OWO:
               await bot.send_message(
                    CRINGE_LOGS,
                    f"""/fban {user} {reason}""")              
               await bot.send_message(
                    CRINGE_LOGS,
                    f"""/gban {user} {reason}""")
               await bot.send_message(-1001648239341,
                    f"""
#BANNED
**USER**: [{user}](tg://user?id={user})
**REASON**: {reason}
**ENFORCER**: [{enforcer}](tg://user?id={enforcer})
**CHAT_ID** : {m.chat.id}
""")
            else:
                await m.reply("WTF 😑 Cringe Heros Cant Be Banned! Muditu poda muta kuthi")

    if m.from_user.id in OWO and m.reply_to_message:
        user = m.reply_to_message.from_user.id
        reason = m.text.replace(m.text.split(" ")[0], "")
        enforcer = m.from_user.id

        if not user in OWO:
            await add_gban_user(user)
            await bot.send_message(CRINGE_LOGS,
                                   f"""/gban {user} {reason}""")
            await bot.send_message(CRINGE_LOGS,
                                   f"""/fban {user} {reason}""")
            await bot.send_message(-1001648239341,
                                   f"""
#BANNED
**USER**: [{user}](tg://user?id={user})
**REASON**: {reason}
**ENFORCER**: [{enforcer}](tg://user?id={enforcer})
**CHAT_ID** : {m.chat.id}
**Message Link : {m.link}
""")

        else:
            await m.reply("Cringe can't be banned!")
