from pyrogram import filters, Client
from KawaiiXRobot import bot, db

@bot.on_message(filters.command(["proof"], ['/', ".", "?"]))
async def proof(client, message):
    data_id = message.text.split(None, 1)[1]
    if len(message.command) <1:
       await message.reply_text("`Usage:` `/proof 1 fuck`")
    elif len(message.command) <2:
       await message.reply_text("`Give Proof For The Given Id")
    if message.reply_to_message:
       store = message.reply_to_message.text
    else:
       store = message.text.split(None, 2)[2]
    if db.get_proof(data_id)['status'] == True:
       await message.reply_text("`The Proof For This Id Was Already Added Remove The Proof And Try Again`")
    elif db.get_proof(data_id)['status'] == False:
       await db.add_proof(data_id, store)
       await message.reply_text("**Sucessfullyb Stored Data For** `{}`".format(data_id))
       
       
