from pyrogram import filters, types
from pyrogram.types import MessageEntity
from KawaiiXRobot import bot
from KawaiiXRobot.utils.ins_db import ins_db


async def process_ins(message: types.Message, status: str):
    chat_id = message.chat.id
    if reply := message.reply_to_message:
        user_id = reply.from_user.id
        key = (
            await ins_db.add_ins(chat_id, user_id)
            if status == "add"
            else await ins_db.del_ins(chat_id, user_id)
        )
        return await message.reply(await gm(chat_id, key))
    if users := message.command[1:]:
        for user in users:
            user_ids = str(user)
            if user_ids.isnumeric():
                user_id = int(user_ids)
            elif isinstance(user_ids, MessageEntity) and user_ids.user:
                user_id = user_ids.user.id
            else:
                user_id = (await message.chat.get_member(user_ids)).user.id
            key = (
                await ins_db.add_ins(chat_id, user_id)
                if status == "add"
                else await ins_db.del_ins(chat_id, user_id)
            )
            return await message.reply(await gm(chat_id, key))
    user = message.command[1]
    if user.startswith("@"):
        user_id = (await message.chat.get_member(user)).user.id
        key = (
            await ins_db.add_ins(chat_id, user_id)
            if status == "add"
            else await ins_db.del_ins(chat_id, user_id)
        )
        return await message.reply(await gm(chat_id, key))
    if isinstance(user, MessageEntity) and user.user:
        user_id = user.user.id
        key = (
            await ins_db.add_ins(chat_id, user_id)
            if status == "add"
            else await ins_db.del_ins(chat_id, user_id)
        )
        return await message.reply(await gm(chat_id, key))
    if isinstance(user, int):
        user_id = user
        key = (
            await ins_db.add_ins(chat_id, user_id)
            if status == "add"
            else await ins_db.del_inschat_id, user_id)
        )
        return await message.reply(await gm(chat_id, key))


@bot.on_message(filters.command("add"))
@authorized_only
async def add_ins_(_, message: types.Message):
    await process_ins(message, "add")


@bot.on_message(filters.command("delins"))
@authorized_only
async def del_ins_(_, message: types.Message):
    await process_ins(message, "delete")

