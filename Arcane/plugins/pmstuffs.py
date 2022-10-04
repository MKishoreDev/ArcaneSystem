import asyncio 

from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
)
from pyrogram import filters
from Arcane import bot, PREFIX
from Arcane.media import ANIMATION_MEDIA, START_MEDIA
from Arcane.buttons import START_BUTTON

@bot.on_message(filters.command(["start"], PREFIX))
async def start(_, m: Message):
    kk = await m.reply_photo(ANIMATION_MEDIA, caption="`[▒▒▒▒▒▒▒▒▒▒▒▒▒▒]` `0%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[████▒▒▒▒▒▒▒▒▒▒]` `20%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[██████▒▒▒▒▒▒▒▒]` `40%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[████████▒▒▒▒▒▒]` `60%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[██████████▒▒▒▒]` `80%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[███████████████]` `100%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[COMPLETED]`")
    await asyncio.sleep(1)
    await kk.delete()     
    await m.reply_video(
        START_MEDIA,
        caption=START_STRING.format(
            m.from_user.mention
        ),
        reply_markup=InlineKeyboardMarkup(START_BUTTON),
    )
