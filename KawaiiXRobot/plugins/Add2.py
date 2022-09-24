from pyrogram import filters
from pyrogram.types import Message

from KawaiiXRobot import Inspector, bot, eor
from KawaiiXRobot.utils.errors import capture_err
from KawaiiXRobot.utils.add_ins import add_Inspector, get_Inspector, remove_Inspector

COMMANDS = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]

BOT_ID = 5620916588

@bot.on_message(filters.command("useradd", COMMANDS) & SUDOERS)
@capture_err
async def useradd(_, message: Message):
    if not message.reply_to_message:
        return await eor(
            message,
            text="Reply to someone's message to add him to sudoers.",
        )
    user_id = message.reply_to_message.from_user.id
    umention = (await bot.get_users(user_id)).mention
    Inspector = await get_Inspector()

    if user_id in Inspector:
        return await eor(message, text=f"{umention} is already in sudoers.")
    if user_id == BOT_ID:
        return await eor(
            message, text="You can't add assistant bot in sudoers."
        )

    await add_Inspector(user_id)

    if user_id not in Inspector:
        Inspector.add(user_id)

    await eor(
        message,
        text=f"Successfully added {umention} in sudoers.",
    )
