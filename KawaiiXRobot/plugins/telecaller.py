from pyrogram.types import InputPhoneContact
from pyrogram import filters
from KawaiiXRobot import ubot

@ubot.on_message(filters.command("find"))
async def find(_, message):
              elif message.reply_to_message:
                  Numb = message.text.replace("/find", "")
                  await ubot.send_message([InputPhoneContact(f"{Numb}", "Foo")])
      
