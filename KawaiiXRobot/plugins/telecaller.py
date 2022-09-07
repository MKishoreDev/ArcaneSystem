from pyrogram.types import InputPhoneContact
from pyrogram import filters
from KawaiiXRobot import ubot

@ubot.on_message(filters.command("find"))
async def phonenumber(_, message):
    text = message.text.split(None, 1)[1]
    India = "+91"
    number = await ubot.import_contacts([InputPhoneContact(India, text, "Foo")])
    await message.reply_text(number)
