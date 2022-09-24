import asyncio
import re

from time import time
from pyrogram.errors import FloodWait
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    ChatMemberUpdated,
    ChatPermissions,
    Message,
)

from KawaiiXRobot import Inspector
from KawaiiXRobot import bot as app
from KawaiiXRobot.utils.errors import capture_err
from KawaiiXRobot.utils.db_admins import (
    add_warn,
    get_warn,
    int_to_alpha,
    remove_warns,
    save_filter,
)

COMMANDS = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]

BOT_ID = 5620916588

async def member_permissions(chat_id: int, user_id: int):
    perms = []
    try:
        member = await app.get_chat_member(chat_id, user_id)
    except Exception:
        return []
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_voice_chats:
        perms.append("can_manage_voice_chats")
    return perms


from KawaiiXRobot.core import adminsOnly

admins_in_chat = {}


async def list_admins(chat_id: int):
    global admins_in_chat
    if chat_id in admins_in_chat:
        interval = time() - admins_in_chat[chat_id]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[chat_id]["data"]

    admins_in_chat[chat_id] = {
        "last_updated_at": time(),
        "data": [
            member.user.id
            async for member in app.iter_chat_members(
                chat_id, filter="administrators"
            )
        ],
    }
    return admins_in_chat[chat_id]["data"]


# Admin cache reload


@app.on_chat_member_updated()
async def admin_cache_func(_, cmu: ChatMemberUpdated):
    if cmu.old_chat_member and cmu.old_chat_member.promoted_by:
        admins_in_chat[cmu.chat.id] = {
            "last_updated_at": time(),
            "data": [
                member.user.id
                async for member in app.iter_chat_members(
                    cmu.chat.id, filter="administrators"
                )
            ],
        }
        log.info(f"Updated admin cache for {cmu.chat.id} [{cmu.chat.title}]")


@app.on_message(filters.command("warn", "dwarn", COMMANDS) & ~filters.edited & ~filters.private
)
@adminsOnly("can_restrict_members")
async def warn_user(_, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    chat_id = message.chat.id
    if not user_id:
        return await message.reply_text("I can't find that user.")
    if user_id == BOT_ID:
        return await message.reply_text(
            "I can't warn myself, i can leave if you want."
        )
    if user_id in Inspector:
        return await message.reply_text(
            "You Wanna Warn The Elevated One?, RECONSIDER!"
        )
    if user_id in (await list_admins(chat_id)):
        return await message.reply_text(
            "I can't warn an admin, You know the rules, so do i."
        )
    user, warns = await asyncio.gather(
        app.get_users(user_id),
        get_warn(chat_id, await int_to_alpha(user_id)),
    )
    mention = user.mention
    keyboard = ikb({"🚨  Remove Warn  🚨": f"unwarn_{user_id}"})
    if warns:
        warns = warns["warns"]
    else:
        warns = 0
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if warns >= 2:
        await message.chat.ban_member(user_id)
        await message.reply_text(
            f"Number of warns of {mention} exceeded, BANNED!"
        )
        await remove_warns(chat_id, await int_to_alpha(user_id))
    else:
        warn = {"warns": warns + 1}
        msg = f"""
**Warned User:** {mention}
**Warned By:** {message.from_user.mention if message.from_user else 'Anon'}
**Reason:** {reason or 'No Reason Provided.'}
**Warns:** {warns + 1}/3"""
        await message.reply_text(msg, reply_markup=keyboard)
        await add_warn(chat_id, await int_to_alpha(user_id), warn)


@app.on_callback_query(filters.regex("unwarn_"))
async def remove_warning(_, cq: CallbackQuery):
    from_user = cq.from_user
    chat_id = cq.message.chat.id
    permissions = await member_permissions(chat_id, from_user.id)
    permission = "can_restrict_members"
    if permission not in permissions:
        return await cq.answer(
            "You don't have enough permissions to perform this action.\n"
            + f"Permission needed: {permission}",
            show_alert=True,
        )
    user_id = cq.data.split("_")[1]
    warns = await get_warn(chat_id, await int_to_alpha(user_id))
    if warns:
        warns = warns["warns"]
    if not warns or warns == 0:
        return await cq.answer("User has no warnings.")
    warn = {"warns": warns - 1}
    await add_warn(chat_id, await int_to_alpha(user_id), warn)
    text = cq.message.text.markdown
    text = f"~~{text}~~\n\n"
    text += f"__Warn removed by {from_user.mention}__"
    await cq.message.edit(text)

