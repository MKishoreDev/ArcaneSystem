
from pyrogram import filters
from pyrogram.types import Message

from KawaiiXRobot import BOT_ID, Inspector, bot, DEVS
from KawaiiXRobot.utils.add_ins import add_inspector, get_inspectorers, remove_inspector

COMMANDS = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]

@bot.on_message(filters.command("useradd", COMMANDS) & DEVS)
async def useradd(_, message: Message):
    if not message.reply_to_message:
        return await eor(
            message,
            text="Reply to someone's message to add him to inspectorers.",
        )
    user_id = message.reply_to_message.from_user.id
    umention = (await bot.get_users(user_id)).mention
    inspectorers = await get_inspectorers()

    if user_id in inspectorers:
        return await eor(message, text=f"{umention} is already in inspectorers.")
    if user_id == BOT_ID:
        return await eor(
            message, text="You can't add assistant bot in inspectorers."
        )

    await add_inspector(user_id)

    if user_id not in inspectorERS:
        inspectorERS.add(user_id)

    await eor(
        message,
        text=f"Successfully added {umention} in inspectorers.",
    )


@bot.on_message(filters.command("userdel", COMMANDS) & DEVS)
async def userdel(_, message: Message):
    if not message.reply_to_message:
        return await eor(
            message,
            text="Reply to someone's message to remove him to inspectorers.",
        )
    user_id = message.reply_to_message.from_user.id
    umention = (await bot.get_users(user_id)).mention

    if user_id not in await get_inspectorers():
        return await eor(message, text=f"{umention} is not in inspectorers.")

    await remove_inspector(user_id)

    if user_id in inspectorERS:
        inspectorERS.remove(user_id)

    await eor(
        message,
        text=f"Successfully removed {umention} from inspectorers.",
    )


@bot.on_message(filters.command("inspectorers", COMMANDS) & DEVS)
async def inspectorers_list(_, message: Message):
    inspectorers = await get_inspectorers()
    text = ""
    j = 0
    for user_id in inspectorers:
        try:
            user = await bot.get_users(user_id)
            user = user.first_name if not user.mention else user.mention
            j += 1
        except Exception:
            continue
        text += f"{j}. {user}\n"
    if text == "":
        return await eor(message, text="No inspectorers found.")
    await eor(message, text=text)
