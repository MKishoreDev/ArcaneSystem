from pyrogram.types import InputPhoneContact
from KawaiiXRobot import ubot

@ubot.on_message(filters.command("find"))
async def find(client, message):
cmd = message.text.split(" ", maxsplit=1)[1]
Number = import_contacts([InputPhoneContact(f"{cmd}, "Foo")])
         await ubot.send_message(f"{Number})
