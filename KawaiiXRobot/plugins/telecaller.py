from pyrogram.types import InputPhoneContact
from KawaiiXRobot import ubot

@ubot.on_message(filters.command("find"))
async def find(client, message):
cmd = message.text.split(" ", maxsplit=1)[1]
      await ubot.send_message([InputPhoneContact(f"{cmd}, "Foo")])
      
