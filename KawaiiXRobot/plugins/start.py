import random
from pyrogram import Client
from pyrogram import filters
from KawaiiXRobot import bot
from random import shuffle
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

HMF_VID = (
      "https://telegra.ph/file/65239f3043ca5161617df.mp4",
  )


PM_START_TEXT = """
**Hᴇʟʟᴏ!  Tʜᴇʀᴇ  I  Aᴍ  Cʀɪɴɢᴇ  °  Sʏsᴛᴇᴍ  Tʜᴇ  Jᴜᴅɢᴇᴍᴇɴᴛ  Eɴғᴏʀᴄɪɴɢ  Sʏsᴛᴇᴍ

Iɴᴠᴀᴅᴇᴅ  Aɴᴀʟʏsɪs  Rᴇᴘᴏʀᴛ :-
 ➛ Usᴇʀ: 
 ➛ Iᴅ:
 ➛ Gʙᴀɴɴᴇᴅ
 ➛ Sᴛᴀᴛᴜs:**
"""
buttons = [
    [
        InlineKeyboardButton("Rᴇᴘᴏʀᴛ Eʀʀᴏʀ", url="https://t.me/+u-YFXF8x-Rw0M2Rl"),
        InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+u-YFXF8x-Rw0M2Rl"),
    ],
    [
        InlineKeyboardButton(" Cᴏᴍᴍᴀɴᴅs  Aɴᴅ  Hᴇʟᴘ", callback_data="bhelp"),   
    ],
]



HELP = """
Wᴇʟᴄᴏᴍᴇ  Tᴏ  Cʀɪɴɢᴇ  Hᴇʟᴘ  Sʏsᴛᴇᴍ,  Cʜᴇᴄᴋᴏᴜᴛ  Bᴇʟᴏᴡ  Bᴜᴛᴛᴏɴs  As  Pᴇʀ  Yᴏᴜʀ  Nᴇᴇᴅ.
"""
help_buttons = [
            [
                InlineKeyboardButton("Sᴄᴀɴ", callback_data="scan"),
                InlineKeyboardButton("Jᴜᴍʙʟᴇᴅ 🆎", callback_data="j_help"),
            ],
            [
                InlineKeyboardButton("❮ Nᴇxᴛ", callback_data="p_help"),
                InlineKeyboardButton("Nᴇxᴛ ❯", callback_data="j_help"),
           ],
        ]


@bot.on_message(filters.command(["start"], ['/', ".", "?"]))
async def start(client, message):
             await m.reply_video(
               photo=random.choice(HMF_VID),
                caption=PM_START_TEXT.format(message.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_message(filters.command("help"))
async def start(client, message):
             await m.reply_video(
               photo=random.choice(HMF_VID),
                caption=HELP.format(message.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(help_buttons))


 
