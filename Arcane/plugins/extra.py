# Extra_hmf.py © Copyright By HMF_Owner_1

from pyrogram.types import InputPhoneContact
from pyrogram import filters
from Arcane import ubot

@ubot.on_message(filters.command("find"))
async def phonenumber(_, message):
    text = message.text.split(None, 1)[1]
    number = await ubot.import_contacts([InputPhoneContact("+91" + text, "Foo")])
    await message.reply_text(number)
