from pyrogram import filters, Client
from KawaiiXRobot import bot
from KawaiiXRobot.utils.dbfunctions import get_gbans_count

@bot.on_message(filters.command(["scanlist"], ['/', ".", "?"]))
async def list(client, message):
 try:
    gbans = await get_gbans_count()
    data = await get_gbans_data()
    hehe = "https://telegra.ph/file/65239f3043ca5161617df.mp4"
    await message.reply_video(hehe, caption="`{}` **Globally Scanned/Banned Users**\n\n`{}`".format(gbans, data))
 except Exception:
    pass
