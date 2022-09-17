from KawaiiXRobot import bot, DEVS
from pyrogram import filters
from KawaiiXRobot.utils.filtersdb import (
    remove_proof,
    get_proof,
    get_proof_names,
    save_proof,
)
import re
from KawaiiXRobot.utils.button import get_keyboard
from datetime import datetime, date, time 

def parse_com(com, key):
  try:
    r = com.split(key,1)[1]
  except KeyError:
    return None
  r = (r.split(" ", 1)[1] if len(r.split()) >= 1 else None)
  return r

@bot.on_message(filters.command(["rmproof"], ['/', ".", "?"]))
async def del_proof(_, message):
    if not message.from_user.id in DEVS:
        return 
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n__/rmproof [id]__")
    name = parse_com(message.text, 'rmproof')
    if not name:
        return await message.reply_text("**Usage:**\n__/rmproof [id]__")
    deleted = await remove_proof("/data" + name.strip())
    if deleted:
        await message.reply_text(f"**Deleted Proof {name}.**")
    else:
        await message.reply_text("**No such Proof.**")

@bot.on_message(filters.command(["datalist"], ['/', ".", "?"]))
async def get_datalist(_, message):
    if not message.from_user.id in DEVS:
        return 
    _proofs = await get_proof_names()
    if not _proofs:
        return await message.reply_text("**No Proofs Found.**")
    _proofs.sort()
    msg = f"**List of Proofs**\n"
    for _proof in _proofs:
        hehe = _proof.replace("/data ", "")
        msg += f"**-** `{hehe}`\n"
    await message.reply_text(msg)

@bot.on_message(filters.command(["proof"], ['/', ".", "?"]))
async def save_filters(_, message):
  if not message.from_user.id in DEVS:
    return 
  else:
    if message.text:
      proofy = parse_com(message.text, 'proof')
    elif message.caption:
      proofy = parse_com(message.caption, 'proof')
    else:
      proofy = None
    if not proofy:
      return await message.reply("Give Some Word To save as proof")
    if not (message.reply_to_message) or (len(proofy.split()) < 1):
      return await message.reply("Either reply to a message or give something")
    if message.reply_to_message:
      m = message.reply_to_message
      di = {}
      #di['chat'] = message.chat.id
      di['media'] = m.media
      if m.media:
        di['text'] = m.caption
        if m.photo:
          di['file'] = m.photo.file_id
        elif m.video:
          di['file'] = m.video.file_id
        elif m.sticker:
          di['file'] = m.sticker.file_id
        elif m.document:
          di['file'] = m.document.file_id
        elif m.animation:
          di['file'] = m.animation.file_id
        elif m.audio:
          di['file'] = m.audio.file_id
      else:
        di['text'] = m.text
        di['file'] = None
    else:
      di = {}
      #di['chat'] = message.chat.id
      di['media'] = message.media
      if message.media:
        di['text'] = proofy.split(None, 1)[1]
        if message.photo:
          di['file'] = message.photo.file_id
        elif message.video:
          di['file'] = message.video.file_id
        elif message.document:
          di['file'] = message.document.file_id
        elif message.sticker:
          di['file'] = message.sticker.file_id
        elif message.animation:
          di['file'] = message.animation.file_id
        elif message.audio:
          di['file'] = message.audio.file_id
      else:
        di['text'] = proofy.split(None, 1)[1]
        di['file'] = None
  chat_id = message.chat.id
  _filter = di
  await save_proof("/data" + proofy.split()[0], di)
  await message.reply_text(f"__**Saved filter {proofy.split()[0]}.**__")

