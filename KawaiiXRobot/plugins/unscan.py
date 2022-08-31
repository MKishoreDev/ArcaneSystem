from KawaiiXRobot import bot, KAWAII_LOGS, DEVS, Inspector, KAWAII_CHANNEL
from pyrogram import filters
from pyrogram import Client
import time
from pyrogram.types import Message
from KawaiiXRobot.utils.dbfunctions import (
    add_gban_user,
    remove_gban_user,
)

from KawaiiXRobot.utils import dbfunctions as x

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
            if len(m.command) <2:
                   return await m.reply_text("give me user ID or username")
            elif len(m.command) <3:
                   return await m.reply_text("give a reason to unscan")
            user_ids = m.text.split(None, 1)]1]
            reason = m.text.split(None, 2)[2]
            user = bot.get_users(user_ids)
            user_id = user.id
            enforcer = m.from_user.id
            if user not in OWO:
                await x.remove_gban_user(user_id)
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

