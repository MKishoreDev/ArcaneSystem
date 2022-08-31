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
                  return await m.reply_text("Only The Users of kawaii Can Use Scan")
            elif len(m.command) <2:
                   return await m.reply_text("give me user ID or username")
            user_ids = m.text.split(None, 1)[1]
            get = bot.get_users(user_ids)
            user_id = get.id
            await x.remove_gban_user(user_id)
            await bot.send_message(KAWAII_LOGS, f"/ungban {user}"),
            await bot.send_message(
                    -1001648239341,
                    f"""
╒═══「 #DestroyDecomposer 」
**➢ Enforcer:** `{enforcer}`
**➢ Target User:** [{user}](tg://user?id={user})
""")
            else:
                await m.reply("Kawaii Fellows Can't Be Revive Bcz They Never Scanned!")
                if message.from_user.id in OWO and message.reply_to_message:
                  enforcer = message.from_user.id
                  user = message.reply_to_message.from_user
                  await x.remove_gban_user(user.id)
                  await bot.send_message(
                    KAWAII_LOGS,
                    f"/ungban {user}"),
                  await bot.send_message(
                    -1001648239341,
                    f"""
╒═══「 #DestroyDecomposer 」
**➢ Enforcer:** `{enforcer}`
**➢ Target User:** [{user}](tg://user?id={user.id})
""")
