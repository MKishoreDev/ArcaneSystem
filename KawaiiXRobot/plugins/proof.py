reason = m.text.split(None, 2)[2]from pyrogram import filters, Client
from KawaiiXRobot import bot, db, DEVS

@bot.on_message(filters.command(["proof"], ['/', ".", "?"]) & filters.user(DEVS))
async def proof(client, message):
    if len(message.command) <1:
       await message.reply_text("`Usage:` `/proof 1 fuck`")
    elif len(message.command) <2:
       await message.reply_text("`Give Proof For The Given Id")
    if message.reply_to_message:
       store = message.reply_to_message.text
       data_id = message.text.split(None, 1)[1]
    if not message.reply_to_message:
       store = message.text.split("", 2)[2]
       data_id = message.text.split(None, 1)[1]
    if db.get_proof(data_id)['status'] == True:
       await message.reply_text("`The Proof For This Id Was Already Added Remove The Proof And Try Again`")
    if db.get_proof(data_id)['status'] != False:
       db.add_proof(data_id, store)
       await message.reply_text("**Sucessfully Stored Data For** `{}`".format(data_id))

@bot.on_message(filters.command(["data"], ['/', ".", "?"]))
async def data(client, message):
    data_id = message.text.split(None, 1)[1]
    if len(message.command) <1:
       await message.reply_text("`Usage:` `/data 1`")
    if db.get_proof(data_id)['status'] == True:
       await message.reply_text(f"Data Of {data_id}\n\n • {db.get_proof(data_id)['proof']}")
    if db.get_proof(data_id)['status'] != True:
       await message.reply_text("**No Such Data Found For** `{}`".format(data_id))
       
       
