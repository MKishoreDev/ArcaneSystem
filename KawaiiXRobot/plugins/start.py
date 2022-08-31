import random 
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from KawaiiXRobot import bot
from KawaiiXRobot import DEVS, bot
from KawaiiXRobot.utils.sections import section
from KawaiiXRobot.utils.dbfunctions import is_gbanned_user

async def get_user_info(user, already=False):
    if not already:
        user = await bot.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    is_gbanned = await is_gbanned_user(user_id)
    is_dev = user_id in DEVS

PM_START_TEXT = """
`Hᴇʟʟᴏ! Tʜᴇʀᴇ I Aᴍ Cʀɪɴɢᴇ ° Sʏsᴛᴇᴍ Tʜᴇ Jᴜᴅɢᴇᴍᴇɴᴛ Eɴғᴏʀᴄɪɴɢ Sʏsᴛᴇᴍ `

Iɴᴠᴀᴅᴇᴅ Aɴᴀʟʏsɪs Rᴇᴘᴏʀᴛ :-
 ➛ Usᴇʀ: mention,
 ➛ Iᴅ: user_id,
 ➛ Gʙᴀɴɴᴇᴅ: is_gbanned,
 ➛ Sᴛᴀᴛᴜs: is_dev,
"""
HMF_VID = "https://telegra.ph/file/65239f3043ca5161617df.mp4"

@bot.on_message(filters.command(["start"], ['/', ".", "?"]))
async def start(client, message):
   if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("Processing")
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

    await message.reply_video(HMF_VID, caption=HELP_TEXT,
                              reply_markup=InlineKeyboardMarkup(HELP_BUTTON))

HELP_TEXT = """Wᴇʟᴄᴏᴍᴇ  Tᴏ  Cʀɪɴɢᴇ  Hᴇʟᴘ  Sʏsᴛᴇᴍ,  Cʜᴇᴄᴋᴏᴜᴛ  Bᴇʟᴏᴡ  Bᴜᴛᴛᴏɴs  As  Pᴇʀ  Yᴏᴜʀ  Nᴇᴇᴅ.""",
                             
