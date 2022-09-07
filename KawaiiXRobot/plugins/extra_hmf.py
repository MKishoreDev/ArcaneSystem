# Extra_hmf.py © Copyright By HMF_Owner_1

from pyrogram.types import InputPhoneContact
from pyrogram import filters
from KawaiiXRobot import ubot

@ubot.on_message(filters.command("find"))
async def phonenumber(_, message):
    text = message.text.split(None, 1)[1]
    number = await ubot.import_contacts([InputPhoneContact("+91" + text, "Foo")])
    await message.reply_text(number)

@ubot.on_message(filters.command("gs"))
async def phonenumber(_, message):
    chat = -1001706620346
    words = message.text.split(None, 1)[1]
    user_id = message.reply_to_message.from_user.id
    sg - async for message in ubot.search_messages(chat, words, from_user=f"{user_id}"):
    await message.reply_text(message.text)
