import random
from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

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

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(_, m):
             await m.reply_video(
               photo=random.choice(HMF_VID),
                caption=PM_START_TEXT.format(m.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_message(filters.command("help"))
async def help(_, m):
             await m.reply_video(
               photo=random.choice(HMF_VID),
                caption=HELP.format(m.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(help_buttons))


 
@Client.on_callback_query(filters.regex("bstart"))
async def bstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hᴇʟʟᴏ,  Wᴇʟᴄᴏᴍᴇ  Tᴏ  Mᴀᴊᴇsᴛʏ  Wᴏʀᴅ  Bᴏᴛ,  Yᴏᴜ  Cᴀɴ  Pʟᴀʏ  Wᴏʀᴅ  Dᴇʀɪᴠᴀᴛɪᴏɴ  Gᴀᴍᴇ  Oʀ  Wᴏʀᴅ  Nᴀʀʀᴀᴛɪᴏɴ  Wɪᴛʜ  Tʜɪs  Bᴏᴛ ✨.

➤  Cʟɪᴄᴋ  👉  /help  Fᴏʀ  Iɴғᴏʀᴍᴀᴛɪᴏɴ. ᴛʜᴇ  Cᴏᴍᴍᴀɴᴅs  Aʀᴇ  Eᴀsʏ  Aɴᴅ  Sɪᴍᴘʟᴇ 💖

➤  Eɴᴊᴏʏ  Wɪᴛʜ  Yᴏᴜʀ  Fʀɪᴇɴᴅs ✨..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("➕ Aᴅᴅ  Tᴏ  Yᴏᴜʀ  Gʀᴏᴜᴘ ➕", url=f"http://t.me/DolphinGameBot?startgroup=new")
                ],
                [
                    InlineKeyboardButton("📢  Uᴘᴅᴀᴛᴇs", url="https://t.me/+u-YFXF8x-Rw0M2Rl"),
                    InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ ⚠️", url="https://t.me/+u-YFXF8x-Rw0M2Rl"),
                ],
                [
                    InlineKeyboardButton("📚  Cᴏᴍᴍᴀɴᴅs  Aɴᴅ  Hᴇʟᴘ  📚", callback_data="bhelp"),   
                ],
             ]
         ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("bhelp"))
async def bhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hɪ ! I'ᴍ [Dᴏʟᴘʜɪɴ 🐬](https://t.me/DolphinGameBot)  Bᴀsᴇᴅ Oɴ Gᴀᴍᴇ Bᴏᴛ 🇺🇸

I Hᴀᴠᴇ Tᴏᴛᴀʟʟʏ 2 Gᴀᴍᴇ Eɴᴊᴏʏ Wɪᴛʜ Yᴏᴜʀ Fʀɪᴇɴᴅs 🥳""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✍ Pᴀʀᴀᴘʜʀᴀsᴇ", callback_data="p_help"),
                    InlineKeyboardButton("Jᴜᴍʙʟᴇᴅ 🆎", callback_data="j_help"),
                ],
                [
                    InlineKeyboardButton("❮ Nᴇxᴛ", callback_data="p_help"),
                    InlineKeyboardButton("🔙 Gᴏ Bᴀᴄᴋ", callback_data="bstart"),  
                    InlineKeyboardButton("Nᴇxᴛ ❯", callback_data="j_help"),
                ],
             ]
         ),
         disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("scan"))
async def phelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""How to scan 

👉🏻 1st case if scanning the user via replying to that user message,
Use command /scan + flags checkout flags button.

E.g /scan -r threat -p https://telegra.ph/media

👉🏻 2nd case if scanning the user via "message link/username/user id"
Use command /scan -id + flags checkout flags button.

E.g /scan -id 1234560914 -r threat -p https://telegra.ph/media""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴏ Bᴀᴄᴋ", callback_data="bhelp"),
              InlineKeyboardButton("Nᴇxᴛ ❯", callback_data="j_help")]]
        ),
    )

@Client.on_callback_query(filters.regex("j_help"))
async def jhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🐬  [ **Pᴀʀᴀᴘʜʀᴀsᴇ Wᴏʀᴅs Gᴀᴍᴇ Cᴍᴅ** ] 🇺🇸

/game_2  -  Sᴛᴀʀᴛ  Pᴀʀᴀᴘʜʀᴀsᴇ  Wᴏʀᴅs  Gᴀᴍᴇ

/pass  -  Tᴏ  Pᴀss  Cᴜʀʀᴇɴᴛ  Pᴀʀᴀᴘʜʀᴀsᴇ  Wᴏʀᴅ

/cancel  -  Tᴏ  Cᴀɴᴄᴇʟ  Pᴀʀᴀᴘʜʀᴀsᴇ  Wᴏʀᴅs  Gᴀᴍᴇ

/rules  -  Tᴏ  Sᴇᴇ  Gᴀᴍᴇ  Rᴜʟᴇs""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("❮ Nᴇxᴛ", callback_data="p_help"),
              InlineKeyboardButton("🔙 Gᴏ Bᴀᴄᴋ", callback_data="bhelp")]]
        ),
    )
