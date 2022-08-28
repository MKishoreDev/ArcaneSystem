from KawaiiXRobot import bot, KAWAII_LOGS, DEVS, Inspector, KAWAII_CHANNEL
from pyrogram import filters
from pyrogram import Client
import time
from pyrogram.types import Message
from KawaiiXRobot.utils.dbfunctions import (
    add_gban_user,
    remove_gban_user,
)

OWO = DEVS + Inspector

@bot.on_message(filters.command(["re(vive|vert|store)"], prefixes=["/", ".", "?", "-"]))
async def revive(Client, m: Message):
    if m.from_user.id not in OWO:
        await m.reply_text("Only The Users of kawaii Can Use Scan")
        return

    if not m.reply_to_message:
        user = " ".join(m.command[1:])
        enforcer = m.from_user.id
        if not user.isdigit():
            await m.reply_text("User ID Must Be Integer")
            return

        else:
            user = " ".join(m.command[1:])
            enforcer = m.from_user.id
            if user not in OWO:
                await remove_gban_user(user)
                await bot.send_message(
                    KAWAII_LOGS,
                    f"/ungban {user}"),
                await bot.send_message(
                    -1001648239341,
                    f"""
╒═══「 #DestroyDecomposer 」
**➢ Enforcer:** `{enforcer}`
**➢ Target User:** [{user}](tg://user?id={user})
**➢ Reason:** `{reason}`
""")
            else:
                await m.reply("Kawaii Fellows Can't Be Revive Bcz They Never Scanned!")

    if m.from_user.id in OWO and m.reply_to_message:
        user = m.reply_to_message.from_user.id
        enforcer = m.from_user.id
        if user not in OWO:
             await remove_gban_user(user)
             await bot.send_message(
                 KAWAII_LOGS,
                 f"/ungban {user}"),
             await bot.send_message(
                 -1001648239341,
                 f"""
╒═══「 #DestroyDecomposer 」
**➢ Enforcer:** `{enforcer}`
**➢ Target User:** [{user}](tg://user?id={user})
**➢ Reason:** <tg-spoiler>Secret</tg-spoiler>
""")
