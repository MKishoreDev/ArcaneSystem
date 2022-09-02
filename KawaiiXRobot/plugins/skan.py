from KawaiiXRobot import bot, KAWAII_LOGS, DEVS, Inspector, KAWAII_CHANNEL, ubot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
import time
from pyrogram.types import Message
from KawaiiXRobot.utils.dbfunctions import (
    add_gban_user,
)

OWO = DEVS + Inspector

@bot.on_message(filters.command("skan", prefixes=["/", ".", "?", "-"]))
async def ban(Client, m: Message):
    if m.from_user.id not in OWO:
        await m.reply_text("Only The Vampire of Blue moon Can Use Me")

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
            user = int(user)
            if user not in OWO:
                await add_gban_user(user)
            elif user not in OWO:
               await ubot.send_message(
                    -1001781501832,
                    f"""/fban {user} {reason}""")              
               await ubot.send_message(
                    -1001781501832,
                    f"""/gban {user} {reason}""")
               await  m.reply_text("Connection To Cringe All Bot... Successfully Scanned.")
               await bot.send_message(-1001648239341,
                    f"""
#BANNED
**USER**: [{user}](tg://user?id={user})
**REASON**: {reason}
**ENFORCER**: [{enforcer}](tg://user?id={enforcer})
**CHAT_ID** : {m.chat.id}
""")
            else:
                await m.reply("Vampires Cant Be Banned!")

    if m.from_user.id in OWO and m.reply_to_message:
        user = m.reply_to_message.from_user.id
        reason = m.text.replace(m.text.split(" ")[0], "")
        enforcer = m.from_user.id

        if user not in OWO:
            user = int(user)
            buttons = [[
                InlineKeyboardButton("Support",
                                     url="https://t.me/PlayBoysDXd"),
            ],
                       [
                           InlineKeyboardButton(
                               "Report", url="https://t.me/playBoysDXD"),
                       ]]
            x = OWO.ban(user, reason, enforcer)
            await bot.send_message(KAWAII_CHANNEL,
                                   f"""
#BANNED

**USER**: [{user}](tg://user?id={user})
**REASON**: {reason}
**ENFORCER**: [{enforcer}](tg://user?id={enforcer})
**CHAT_ID** : {m.chat.id}
**Message Link : {m.link}
""",
                                   reply_markup=InlineKeyboardMarkup(buttons))

        else:
            await m.reply("The Vampire of Blue moon can't be banned!")
