import asyncio
from KawaiiXRobot import bot, db
from pyrogram import filters
from config import DEVS, Inspector, Enforcer

HMF = DEVS + Inspector + Enforcer 

@bot.on_message(filters.command("addproof"))
def proofss(_, m: Message):
    proof = m.text.replace(m.text.split(" ")[0], "")
    if not proof == "":
        db.add_proof(m.from_user.id, proof)
        m.reply("Dᴏɴᴇ!")
    else:
        m.reply("Usᴀɢᴇ : /addproof 12345678 telegraph link")

@bot.on_message(filters.command("proof", ['/', ".", "?"]))
    if db.get_proof(m.from_user.id)['proof'] != True:
        proofs = "Proof Not Stored"

    elif db.get_proof(m.from_user.id)['proof'] == True:
        proofs = db.get_role(m.from_user.id)['proof']

    else:
        proofs = "Proof Not Stored"

    if m.from_user.id in HMF:
        dev_text = f"""
• Proof: {proofs}
"""
    await m.reply(text)
