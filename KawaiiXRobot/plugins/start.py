import random 
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from KawaiiXRobot import bot


PM_START_TEXT = """
`Hᴇʟʟᴏ!  Tʜᴇʀᴇ  I  Aᴍ  Cʀɪɴɢᴇ  °  Sʏsᴛᴇᴍ  Tʜᴇ  Jᴜᴅɢᴇᴍᴇɴᴛ  Eɴғᴏʀᴄɪɴɢ  Sʏsᴛᴇᴍ `

Iɴᴠᴀᴅᴇᴅ  Aɴᴀʟʏsɪs  Rᴇᴘᴏʀᴛ :-
 ➛ Usᴇʀ: 
 ➛ Iᴅ:
 ➛ Gʙᴀɴɴᴇᴅ
 ➛ Sᴛᴀᴛᴜs:**
"""
HMF_VID = "https://telegra.ph/file/65239f3043ca5161617df.mp4"

@bot.on_message(filters.command(["start"], ['/', ".", "?"]))
async def start(client, message):
    START_BUTTON = [
    [
        InlineKeyboardButton("Rᴇᴘᴏʀᴛ Eʀʀᴏʀ", url="https://t.me/+u-YFXF8x-Rw0M2Rl"),
        InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+u-YFXF8x-Rw0M2Rl"),
    ],
    [
        InlineKeyboardButton(" Cᴏᴍᴍᴀɴᴅs  Aɴᴅ  Hᴇʟᴘ", callback_data="bhelp"),   
    ],
]

    await message.reply_video(HMF_VID, caption=PM_START_TEXT.format(message.from_user.mention),
                             reply_markup=InlineKeyboardMarkup(START_BUTTON))

@bot.on_message(filters.command(["help"], ['/', ".", "?"]))
async def help(client, message):
    HELP_BUTTON = [
            [
                InlineKeyboardButton("Sᴄᴀɴ", callback_data="scan"),
                InlineKeyboardButton("Exᴛʀᴀ", callback_data="j_help"),
            ],
            [
                InlineKeyboardButton("Bᴀɴᴄᴏᴅᴇs", callback_data="p_help"),
                InlineKeyboardButton("Cʟᴏsᴇ", callback_data="j_help"),
           ],
        ]

    await message.reply_video(HMF_VID, caption=HELP_TEXT.format(message.from_user.mention),
                              reply_markup=InlineKeyboardMarkup(HELP_BUTTON))

HELP_TEXT = """Wᴇʟᴄᴏᴍᴇ  Tᴏ  Cʀɪɴɢᴇ  Hᴇʟᴘ  Sʏsᴛᴇᴍ,  Cʜᴇᴄᴋᴏᴜᴛ  Bᴇʟᴏᴡ  Bᴜᴛᴛᴏɴs  As  Pᴇʀ  Yᴏᴜʀ  Nᴇᴇᴅ.""",
                             
