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

@bot.on_message(filters.command("revert"))
async def revive(_, message):
          if message.from_user.id not in OWO:
                return await message("Only OWO user can use")
          elif len(message.command) <2:
                return await message.reply("give a user ID or name")
          user_id_text = message.text.split(None, 1)[1]
          get = bot.get_users(user_id_text)
          await x.remove_gban_user(get.id)
          await bot.send_message(-1001648239341,
                    text=f"""
╒═══「 #DestroyDecomposer 」
**➢ Enforcer:** `{message.from_user.id}`
**➢ Target User:** [{user}](tg://user?id={get.id})
""")
          
