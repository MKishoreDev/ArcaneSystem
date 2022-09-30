# Start.py ©Copyright By @HMF_Owner_1

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
COMMANDS = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]

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
        InlineKeyboardButton(" Cᴏᴍᴍᴀɴᴅs  Aɴᴅ  Hᴇʟᴘ", callback_data="back_help"),   
    ],   
    [
        InlineKeyboardButton("Rᴜʟᴇs", callback_data="Rules"),   
    ],   
]

@bot.on_message(filters.command("start", COMMANDS))
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


@bot.on_message(filters.command("help", COMMANDS))
async def help(client, message):
    HELP_TEXT = """Wᴇʟᴄᴏᴍᴇ  Tᴏ  Cʀɪɴɢᴇ  Hᴇʟᴘ  Sʏsᴛᴇᴍ,  Cʜᴇᴄᴋᴏᴜᴛ  Bᴇʟᴏᴡ  Bᴜᴛᴛᴏɴs  As  Pᴇʀ  Yᴏᴜʀ  Nᴇᴇᴅ.""",

    HELP_BUTTON = [
            [
                InlineKeyboardButton("Sᴄᴀɴ", callback_data="scan_help"),
                InlineKeyboardButton("Exᴛʀᴀ", callback_data="extra"),
            ],
            [
                InlineKeyboardButton("Bᴀɴᴄᴏᴅᴇs", callback_data="bancodes"),
                InlineKeyboardButton("Cʟᴏsᴇ", callback_data="delete"),
           ],
        ]

    await message.reply_video(START_VID, caption=HELP_TEXT,
                              reply_markup=InlineKeyboardMarkup(HELP_BUTTON))


@bot.on_callback_query(filters.regex("scan_help"))
async def scanhelp(_, query: CallbackQuery):
    await query.edit_message_caption("""How to scan 

👉🏻 1st case if scanning the user via replying to that user message,
Use command /scan + flags checkout flags button.

`E.g /scan -r threat -p https://telegra.ph/media`

👉🏻 2nd case if scanning the user via "message link/username/user id"
Use command /scan -id + flags checkout flags button.

`E.g /scan -id 1234560914 -r threat -p https://telegra.ph/media`""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("Sᴄᴀɴ", callback_data="scan_help"),
                InlineKeyboardButton("Exᴛʀᴀ", callback_data="extra"),
            ],
            [
                InlineKeyboardButton("Bᴀɴᴄᴏᴅᴇs", callback_data="bancodes_help"),
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="back_help"),
                ],
             ]
         ))
        
    

@bot.on_callback_query(filters.regex("bancodes_help"))
async def bancodes(_, query: CallbackQuery):
    await query.edit_message_caption("""Here is Help for **Bancodes** :-
**✯** `{CGX00}` **SCAMMER.**
**✯** `{CGX01}` **SPAM ADDING MEMBER.**
**✯** `{CGX03}` **ABUSE SPAM.**
**✯** `{CGX04}` **NSFW SPAMMER.**
**✯** `{CGX06}` **IMPERSONATION.**
**✯** `{CGX07}` **MD/BTC SCAM.**
**✯** `{CGX08}` **ADDING SPAMBOTS.**
**✯** `{CGX10}` **ILLEGAL.**
**✯** `{CGX11}` **PHISHING.**
**✯** `{CGX12}` **FRAUD PROMOTION  [ANY KIND].**
**✯** `{CGX13}` **CYBER THREATENING / CYBER BULLY.**
**✯** `{CGX14}` **CHILD ABUSE.**
**✯** `{CGX15}` **BAN EVASION.**
**✯** `{CGX16}` **SPAMBOT.**
**✯** `{CGX17}` **RAID INITIALIZOR.** 
**✯** `{CGX18}` **RAID PARTICIPANT.**
**✯** `{CGX19}` **KRIMINALANT.**
**✯** `{CGX20}` **SPAMMING VIOLENT CONTENT.**
**✯** `{CGX21}` **HATE SPEECH AGAINST NATIONALITY.**
**✯** `{CGX22}` **RAID/SPAM INFLAMMER.**
**✯** `{CGX23}` **PRONOGRAPHY CCONTENT PROMOTING.**
**✯** `{CGX24}` **PAID GIRL.**
""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("Sᴄᴀɴ", callback_data="scan_help"),
                InlineKeyboardButton("Exᴛʀᴀ", callback_data="extra"),
            ],
            [
                InlineKeyboardButton("Bᴀɴᴄᴏᴅᴇs", callback_data="bancodes_help"),
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="back_help"),
                ],
             ]
         ))
        

@bot.on_callback_query(filters.regex("back_help"))
async def helpback(_, query: CallbackQuery):
    await query.edit_message_caption("""Wᴇʟᴄᴏᴍᴇ  Tᴏ  Cʀɪɴɢᴇ  Hᴇʟᴘ  Sʏsᴛᴇᴍ,  Cʜᴇᴄᴋᴏᴜᴛ  Bᴇʟᴏᴡ  Bᴜᴛᴛᴏɴs  As  Pᴇʀ  Yᴏᴜʀ  Nᴇᴇᴅ.""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("Sᴄᴀɴ", callback_data="scan_help"),
                InlineKeyboardButton("Exᴛʀᴀ", callback_data="extra"),
            ],
            [
                InlineKeyboardButton("Bᴀɴᴄᴏᴅᴇs", callback_data="bancodes_help"),
                InlineKeyboardButton("Cʟᴏsᴇ", callback_data="delete"),
                ],
             ]
         ))
        
    
@bot.on_callback_query(filters.regex("back_start"))
async def startback(_, query: CallbackQuery):
    await query.edit_message_caption("""`Hᴇʟʟᴏ! Tʜᴇʀᴇ I Aᴍ Cʀɪɴɢᴇ ° Sʏsᴛᴇᴍ Tʜᴇ Jᴜᴅɢᴇᴍᴇɴᴛ Eɴғᴏʀᴄɪɴɢ Sʏsᴛᴇᴍ `
Iɴᴠᴀᴅᴇᴅ Aɴᴀʟʏsɪs Rᴇᴘᴏʀᴛ :-
 ➛ Usᴇʀ: {m.from_user.first_name}
 ➛ Iᴅ: {m.from_user.id}
 ➛ Gʙᴀɴɴᴇᴅ: {is_gbanned}
 ➛ Sᴛᴀᴛᴜs: {status}""",
       reply_markup=InlineKeyboardMarkup(
        [
            [
            InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/playBoysDXD"),
            InlineKeyboardButton("Sᴘᴀᴍ ʀᴇᴘᴏʀᴛ", url="https://t.me/playBoysDXD"),
        ],
        [
            InlineKeyboardButton(" Cᴏᴍᴍᴀɴᴅs  Aɴᴅ  Hᴇʟᴘ", callback_data="back_help"),   
           ],
        ]
     ))

@bot.on_callback_query(filters.regex("delete"))
async def delete(_, query):
    await query.message.delete()

@bot.on_message(filters.command("rules", COMMANDS))
async def rules(client, message):
    RULES_TEXT = """Oᴜʀ Sᴄᴀɴɴᴇʀ Rᴜʟᴇs Fᴏʀ Aʟʟ Oᴜʀ Tᴇʟᴇɢʀᴀᴍ Mᴇᴍʙᴇʀs""",
    RULES_IMG = "https://telegra.ph/file/80f59b1adfd42a368552a.jpg"
    RULES_BUTTON = [
            [
                InlineKeyboardButton("Bᴀsɪᴄ Rᴜʟᴇs", callback_data="basic_scanner_rules"),
                InlineKeyboardButton("Hᴜᴍᴀɴ Rᴜʟᴇs", callback_data="Girls_Safe_Rule"),
            ],
            [
                InlineKeyboardButton("Tᴏxɪᴄ Rᴜʟᴇs", callback_data="Toxic_Boom"),
                InlineKeyboardButton("Gʀᴏᴜᴘ Rᴜʟᴇs", callback_data="group_rules"),
            ],
            [
                InlineKeyboardButton("Cʟᴏsᴇ", callback_data="delete"),
           ],
        ]

    await message.reply_photo(RULES_IMG, caption=RULES_TEXT,
                              reply_markup=InlineKeyboardMarkup(RULES_BUTTON))

@bot.on_callback_query(filters.regex("Rules"))
async def rules(_, query: CallbackQuery):
    await query.edit_message_caption("""Oᴜʀ Sᴄᴀɴɴᴇʀ Rᴜʟᴇs Fᴏʀ Aʟʟ Oᴜʀ Tᴇʟᴇɢʀᴀᴍ Mᴇᴍʙᴇʀs""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("Bᴀsɪᴄ Rᴜʟᴇs", callback_data="basic_scanner_rules"),
                InlineKeyboardButton("Hᴜᴍᴀɴ Rᴜʟᴇs", callback_data="Girls_Safe_Rule"),
            ],
            [
                InlineKeyboardButton("Tᴏxɪᴄ Rᴜʟᴇs", callback_data="Toxic_Boom"),
                InlineKeyboardButton("Gʀᴏᴜᴘ Rᴜʟᴇs", callback_data="group_rules"),
            ],
            [
                InlineKeyboardButton("Cʟᴏsᴇ", callback_data="delete"),
                ],
             ]
         ))
        
@bot.on_callback_query(filters.regex("basic_scanner_rules"))
async def basichelp(_, query: CallbackQuery):
    await query.edit_message_caption("""**Main Sanner**

• `don't scan without reason to anyone`

• `don't scan first check the reason carefully` 

• `don't scan private chat because were don't trust private things`

• `don't give reason with clear pornography proof Hide and add reason`""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("Bᴀsɪᴄ Rᴜʟᴇs", callback_data="basic_scanner_rules"),
                InlineKeyboardButton("Hᴜᴍᴀɴ Rᴜʟᴇs", callback_data="Girls_Safe_Rule"),
            ],
            [
                InlineKeyboardButton("Tᴏxɪᴄ Rᴜʟᴇs", callback_data="Toxic_Boom"),
                InlineKeyboardButton("Gʀᴏᴜᴘ Rᴜʟᴇs", callback_data="group_rules"),
            ],
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="Rules"),
                ],
             ]
         ))
        
@bot.on_callback_query(filters.regex("Girls_Safe_Rule"))
async def girlssafe(_, query: CallbackQuery):
    await query.edit_message_caption("""**Girls And Boys Safe Zone**

• `Don't Abuse Anyone, If You Abuse AnyOne Then You Will Get Ban From AnyOne`

• `Porn Girls And Gay Boys Are Not Allowed In Group`""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("Bᴀsɪᴄ Rᴜʟᴇs", callback_data="basic_scanner_rules"),
                InlineKeyboardButton("Hᴜᴍᴀɴ Rᴜʟᴇs", callback_data="Girls_Safe_Rule"),
            ],
            [
                InlineKeyboardButton("Tᴏxɪᴄ Rᴜʟᴇs", callback_data="Toxic_Boom"),
                InlineKeyboardButton("Gʀᴏᴜᴘ Rᴜʟᴇs", callback_data="group_rules"),
            ],
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="Rules"),
                ],
             ]
         ))
        

@bot.on_callback_query(filters.regex("group_rules"))
async def basicgrouprules(_, query: CallbackQuery):
    await query.edit_message_caption("""**Group Rules**

• `Do not use profanity`

• `Do not advertise without admins permission.`

• `Do not flood the group (No spamming).`

• `Gore, Porn, Hentai or any sort of NSFW is strictly prohibited. Do not put up explicit content.`

• `Do not "disturb" anyone in personal messages.`

• `Do Not use bad Words On VC.`

• `Don't Fight On A personal Reasons. also on a vc you can't.`""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("Bᴀsɪᴄ Rᴜʟᴇs", callback_data="basic_scanner_rules"),
                InlineKeyboardButton("Hᴜᴍᴀɴ Rᴜʟᴇs", callback_data="Girls_Safe_Rule"),
            ],
            [
                InlineKeyboardButton("Tᴏxɪᴄ Rᴜʟᴇs", callback_data="Toxic_Boom"),
                InlineKeyboardButton("Gʀᴏᴜᴘ Rᴜʟᴇs", callback_data="group_rules"),
            ],
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="Rules"),
                ],
             ]
         ))
        

@bot.on_callback_query(filters.regex("Toxic_Boom"))
async def basictoxirules(_, query: CallbackQuery):
    await query.edit_message_caption("""**Group Rules**

• `Do not use profanity`

• `Do not advertise without admins permission.`

• `Do not flood the group (No spamming).`

• `Gore, Porn, Hentai or any sort of NSFW is strictly prohibited. Do not put up explicit content.`

• `Do not "disturb" anyone in personal messages.`

• `Do Not use bad Words On VC.`

• `Don't Fight On A personal Reasons. also on a vc you can't.`""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("Bᴀsɪᴄ Rᴜʟᴇs", callback_data="basic_scanner_rules"),
                InlineKeyboardButton("Hᴜᴍᴀɴ Rᴜʟᴇs", callback_data="Girls_Safe_Rule"),
            ],
            [
                InlineKeyboardButton("Tᴏxɪᴄ Rᴜʟᴇs", callback_data="Toxic_Rules"),
                InlineKeyboardButton("Gʀᴏᴜᴘ Rᴜʟᴇs", callback_data="group_rules"),
            ],
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="Rules"),
                ],
             ]
         ))
        
