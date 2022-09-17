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

@bot.on_message(
    filters.text
    & ~filters.edited
    & ~filters.private
    & ~filters.via_bot
    & ~filters.forwarded,
    group=1,
)
async def filters_re(_, message):
  text = message.text.lower().strip()
  if not text:
    return
  muser = message.from_user
  chat_id = message.chat.id
  list_of_filters = await get_proof_names()
  for word in list_of_proofs:
    pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
    if re.search(pattern, text, flags=re.IGNORECASE):
      proof_msg = await get_proof(word)
      if not proof_msg['media']:
        if proof_msg['text']:
          cap, keyb = get_keyboard(proof_msg['text'])
          cap = cap.format(username="@" + muser.username, mention=f"[{muser.first_name}](tg://user?id={muser.id})", chatname=message.chat.title, firstname=muser.first_name, lastname = muser.last_name, fullname=muser.first_name + (muser.last_name or ""), date=date.today(), time=f"{(datetime.today()).time()}"[:8])
          return await message.reply_text(text=cap, reply_markup=keyb)
      else:
        media = proof_msg['media']
        file = proof_msg['file']
        if media == 'photo':
          func = message.reply_photo
        elif media == 'video':
          func = message.reply_video
        elif media == 'audio':
          func = message.reply_audio
        elif media == 'animation':
          func = message.reply_animation
        elif media == 'document':
          func = message.reply_document
        elif media == 'sticker':
          func = message.reply_sticker
        else:
          func = None
        if proof_msg['text']:
          cap, keyb = get_keyboard(proof_msg['text'])
          if cap:
            cap = proof_msg['text'].format(username="@" + muser.username, mention=f"[{muser.first_name}](tg://user?id={muser.id})", chatname=message.chat.title, firstname=muser.first_name, lastname = muser.last_name, fullname=muser.first_name + (muser.last_name or ""), date=date.today(), time=f"{(datetime.today()).time()}"[:8])
        else:
          cap = None
          keyb = None
        if not func and not cap:
          return
        if func:
          return await func(file, caption=cap, reply_markup=keyb)
