from pyrogram.types import InputPhoneContact
from KawaiiXRobot import ubot

@ubot.on_message(filters.command("find"))
async def find(_, message):
              if len(message.command) <8:
                  await message.reply("Put Correct Number")
                  return 
              elif message.reply_to_message:
                  Numb = message.text.replace("/find", "")
                  await ubot.send_message([InputPhoneContact(f"{Numb}, "Foo")])
      
