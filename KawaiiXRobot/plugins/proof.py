from pyrogram import filters, Client
from KawaiiXRobot import bot, db, DEVS

def parse_com(com, key):
  try:
    r = com.split(key,1)[1]
  except KeyError:
    return None
  r = (r.split(" ", 1)[1] if len(r.split()) >= 1 else None)
  return r

@bot.on_message(filters.command(["proof"], ['/', ".", "?"]) & filters.user(DEVS))
async def proof(client, message):
    data_id = parse_com(message.text, "proof")
    if len(message.command) <1:
       await message.reply_text("`Usage:` `/proof 1 fuck`")
    elif len(message.command) <2:
       await message.reply_text("`Give Proof For The Given Id")
    if not message.reply_to_message:
       store = parse_com(message.text, f"proof {data_id}")
    if message.reply_to_message:
       store = message.reply_to_message.text
    elif message.reply_to_message.sticker:
       store = message.reply_to_message.sticker.file_id
    elif message.reply_to_message.photo:
       store = message.reply_to_message.photo.file_id
    elif message.reply_to_message.audio:
       store = message.reply_to_message.audio.file_id
    elif message.reply_to_message.video:
       store = message.reply_to_message.video.file_id
    elif message.reply_to_message.document:
       store = message.reply_to_message.document.file_id
    elif message.reply_to_message.animation:
       store = message.reply_to_message.animation.file_id
    if db.get_proof(data_id)['status'] == True:
       await message.reply_text("`The Proof For This Id Was Already Added Remove The Proof And Try Again`")
    if db.get_proof(data_id)['status'] != False:
       db.add_proof(data_id, store)
       await message.reply_text("**Sucessfully Stored Data For** `{}`".format(data_id))

@bot.on_message(filters.command(["data"], ['/', ".", "?"]))
async def data(client, message):
    data_id = parse_com(message.text, "data")
    if len(message.command) <1:
       await message.reply_text("`Usage:` `/data 1`")
    if db.get_proof(data_id)['status'] == True:
       await message.reply_text(f"Data Of {data_id}\n\n • {db.get_proof(data_id)['proof']}")
    if db.get_proof(data_id)['status'] != True:
       await message.reply_text("**No Such Data Found For** `{}`".format(data_id))
       
       
