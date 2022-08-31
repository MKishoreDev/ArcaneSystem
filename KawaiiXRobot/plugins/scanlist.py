from pyrogram import filters, Client
from KawaiiXRobot import bot
from KawaiiXRobot.utils.dbfunctions import get_gbans_count

@bot.on_message(filters.command(["scanlist"], ['/', ".", "?"]))
async def list(client, message):
    gbans = await get_gbans_count()
    await message.reply_text(message.chat.id, caption="`{}` **Globally Scanned/Banned Users**".format(get_gbans_count))
