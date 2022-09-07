from pyrogram.types import InputPhoneContact
from KawaiiXRobot import ubot

@bot.on_message(filters.command("find"))
async def find(client, message):
cmd = message.text.split(" ", maxsplit=1)[1]
Number = await ubot.import_contacts([InputPhoneContact(f"{cmd}, "Foo")])

