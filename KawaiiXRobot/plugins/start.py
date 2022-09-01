import os

from pyrogram import filters
from pyrogram.types import Message, CallbackQuery
from config import DEVS, Inspector, Enforcer 
from KawaiiXRobot import bot
from pyrogram import Client
from KawaiiXRobot.utils.sections import section
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from KawaiiXRobot.utils.dbfunctions import is_gbanned_user

HMF = DEVS + Inspector + Enforcer 

async def get_user_info(user, already=False):
    if not already:
        user = await bot.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    dc_id = user.dc_id
    photo_id = user.photo.big_file_id if user.photo else None
    is_dev = user_id in DEVS


START_VID = (
      "https://telegra.ph/file/65239f3043ca5161617df.mp4"
  )

buttons = [
    [
        InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/playBoysDXD"),
        InlineKeyboardButton("Sᴘᴀᴍ ʀᴇᴘᴏʀᴛ", url="https://t.me/playBoysDXD"),
    ],
    [
        InlineKeyboardButton(" Cᴏᴍᴍᴀɴᴅs  Aɴᴅ  Hᴇʟᴘ", callback_data="help"),   
    ],   
]

@bot.on_message(filters.command("start", ['/', ".", "?"]))
async def status(bot, m: Message):
    is_gbanned = await is_gbanned_user(m.from_user.id)
    if m.from_user.id in DEVS:
        status = "**Gᴏᴅ Oғ Cʀɪɴɢᴇ**"

    elif m.from_user.id in Inspector:
        status = "**Iɴsᴘᴇᴄᴛᴏʀ**"

    elif m.from_user.id in Enforcer:
        status = "**Eɴғᴏʀᴄᴇʀ**"

    elif db.get_role(m.from_user.id)['status'] != True:
        status = "Cɪᴠɪʟɪᴀɴ"

    elif db.get_role(m.from_user.id)['status'] == True:
        status = db.get_role(m.from_user.id)['role']

    else:
        status = "Cɪᴠɪʟɪᴀɴ"

    if m.from_user.id in HMF:
        Start_text = f"""
`Hᴇʟʟᴏ! Tʜᴇʀᴇ I Aᴍ Cʀɪɴɢᴇ ° Sʏsᴛᴇᴍ Tʜᴇ Jᴜᴅɢᴇᴍᴇɴᴛ Eɴғᴏʀᴄɪɴɢ Sʏsᴛᴇᴍ `

Iɴᴠᴀᴅᴇᴅ Aɴᴀʟʏsɪs Rᴇᴘᴏʀᴛ :-
 ➛ Usᴇʀ: {m.from_user.first_name}
 ➛ Iᴅ: {m.from_user.id}
 ➛ Gʙᴀɴɴᴇᴅ: {is_gbanned}
 ➛ Sᴛᴀᴛᴜs: {status}"""
        await m.reply_video(
               START_VID,
                caption=Start_text,              
                reply_markup=InlineKeyboardMarkup(buttons))


@bot.on_message(filters.command(["help"], ['/', ".", "?"]))
async def help(client, message):
    HELP_TEXT = """Wᴇʟᴄᴏᴍᴇ  Tᴏ  Cʀɪɴɢᴇ  Hᴇʟᴘ  Sʏsᴛᴇᴍ,  Cʜᴇᴄᴋᴏᴜᴛ  Bᴇʟᴏᴡ  Bᴜᴛᴛᴏɴs  As  Pᴇʀ  Yᴏᴜʀ  Nᴇᴇᴅ.""",

    HELP_BUTTON = [
            [
                InlineKeyboardButton("Sᴄᴀɴ", callback_data="scan_help"),
                InlineKeyboardButton("Exᴛʀᴀ", callback_data="extra"),
            ],
            [
                InlineKeyboardButton("Bᴀɴᴄᴏᴅᴇs", callback_data="bancodes"),
                InlineKeyboardButton("Cʟᴏsᴇ", callback_data="back_start"),
           ],
        ]

    await message.reply_video(START_VID, caption=HELP_TEXT,
                              reply_markup=InlineKeyboardMarkup(HELP_BUTTON))

SCAN_HELP = """ ok
add here 
"""

@Client.on_callback_query(filters.regex("scan_help"))
async def scanhelp(_, query: CallbackQuery):
    await query.edit_message_caption(SCAN_HELP,
       reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("Sᴄᴀɴ", callback_data="scan"),
                InlineKeyboardButton("Exᴛʀᴀ", callback_data="extra"),
            ],
            [
                InlineKeyboardButton("Bᴀɴᴄᴏᴅᴇs", callback_data="bancodes"),
                InlineKeyboardButton("Cʟᴏsᴇ", callback_data="back_start"),
                ],
             ]
         ))
        
    
