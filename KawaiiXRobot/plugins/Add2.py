from pyrogram import filters
from pyrogram.types import Message

from KawaiiXRobot import ENFORCERS, bot, DEVS

@bot.on_message(filters.command("addenf", COMMANDS) & filters.user(DEVS))
def addenf(_, m: Message):
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    if len(message.command) <2:
        user_id = m.text.replace(m.text.split(" ")[0], "")
    if not user_id:
        m.reply_text("`Refer A User First...`")
        return 
    if int(user_id) == DEVS:
        message.reply_text("The specified user is my dev! No need add him to Enforcer list!")
        return ""

    if int(user_id) in ENFORCERS:
        message.reply_text("Buddy this user is already a enforcer user.")
        return ""

    with open("enf_users.txt","a") as file:
        file.write(str(user_id) + "\n")

    ENFORCERS.append(user_id)
    m.reply_text("Succefully Added To SUDO List!")
    return

@bot.on_message(filters.command("rmenf", COMMANDS) & filters.user(DEVS)
def rmenf(_, m: Message):
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    if len(message.command) <2:
        user_id = m.text.replace(m.text.split(" ")[0], "")
    if not user_id:
        m.reply_text("`Refer A User First...`")
        return 
    if int(user_id) == DEVS:
        message.reply_text("The specified user is my dev no need to remove from anything Blah Blah!")
        return ""

    if user_id not in ENFORCERS:
        message.reply_text("Buddy this user is not a enforcer.")
        return ""

    users = [line.rstrip('\n') for line in open("enf_users.txt")]

    with open("enf_users.txt","w") as file:
        for user in users:
            if not int(user) == user_id:
                file.write(str(user) + "\n")

    ENFORCERS.remove(user_id)
    message.reply_text("Yep Succefully removed from Enf List!")
    return
