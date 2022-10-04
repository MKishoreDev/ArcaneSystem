import asyncio 

from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
)
from pyrogram import filters
from Arcane import bot, PREFIX
from Arcane.strings import START_STRING
from Arcane.media import ANIMATION_MEDIA, START_MEDIA
from Arcane.buttons import START_BUTTON, HELP_BUTTON,

@bot.on_message(filters.command(["start"], PREFIX))
async def start(_, m: Message):
    kk = await m.reply_photo(ANIMATION_MEDIA, caption="`[▒▒▒▒▒▒▒▒▒▒▒▒▒▒]` `0%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[████▒▒▒▒▒▒▒▒▒▒]` `20%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[██████▒▒▒▒▒▒▒▒]` `40%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[████████▒▒▒▒▒▒]` `60%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[██████████▒▒▒▒]` `80%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[███████████████]` `100%`")
    await asyncio.sleep(2)
    await kk.edit_caption("`[COMPLETED]`")
    await asyncio.sleep(1)
    await kk.delete()     
    await m.reply_video(
        START_MEDIA,
        caption=START_STRING.format(
            m.from_user.mention
        ),
        reply_markup=InlineKeyboardMarkup(START_BUTTON),
    )

@bot.on_message(filters.command("help", COMMANDS))
async def help(client, message):
    HELP_TEXT = """Wᴇʟᴄᴏᴍᴇ  Tᴏ  Cʀɪɴɢᴇ  Hᴇʟᴘ  Sʏsᴛᴇᴍ,  Cʜᴇᴄᴋᴏᴜᴛ  Bᴇʟᴏᴡ  Bᴜᴛᴛᴏɴs  As  Pᴇʀ  Yᴏᴜʀ  Nᴇᴇᴅ.""",
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
       reply_markup=InlineKeyboardMarkup(SCANHELP_BUTTON))
        
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
       reply_markup=InlineKeyboardMarkup(SCANHELP_BUTTON))

@bot.on_callback_query(filters.regex("back_help"))
async def helpback(_, query: CallbackQuery):
    await query.edit_message_caption("""Wᴇʟᴄᴏᴍᴇ  Tᴏ  Cʀɪɴɢᴇ  Hᴇʟᴘ  Sʏsᴛᴇᴍ,  Cʜᴇᴄᴋᴏᴜᴛ  Bᴇʟᴏᴡ  Bᴜᴛᴛᴏɴs  As  Pᴇʀ  Yᴏᴜʀ  Nᴇᴇᴅ.""",
       reply_markup=InlineKeyboardMarkup(SCANHELP_BUTTON2))
    
@bot.on_callback_query(filters.regex("back_start"))
async def startback(_, query: CallbackQuery):
    await query.edit_message_caption("""`Hᴇʟʟᴏ! Tʜᴇʀᴇ I Aᴍ Cʀɪɴɢᴇ ° Sʏsᴛᴇᴍ Tʜᴇ Jᴜᴅɢᴇᴍᴇɴᴛ Eɴғᴏʀᴄɪɴɢ Sʏsᴛᴇᴍ `
Iɴᴠᴀᴅᴇᴅ Aɴᴀʟʏsɪs Rᴇᴘᴏʀᴛ :-
 ➛ Usᴇʀ: {m.from_user.first_name}
 ➛ Iᴅ: {m.from_user.id}
 ➛ Gʙᴀɴɴᴇᴅ: {is_gbanned}
 ➛ Sᴛᴀᴛᴜs: {status}""",
       reply_markup=InlineKeyboardMarkup(SCANHELP_BUTTON3))

@bot.on_callback_query(filters.regex("delete"))
async def delete(_, query):
    await query.message.delete()

@bot.on_message(filters.command("rules", COMMANDS))
async def rules(client, message):
    RULES_TEXT = """Oᴜʀ Sᴄᴀɴɴᴇʀ Rᴜʟᴇs Fᴏʀ Aʟʟ Oᴜʀ Tᴇʟᴇɢʀᴀᴍ Mᴇᴍʙᴇʀs""",
    await message.reply_photo(RULES_IMG, caption=RULES_TEXT,
                              reply_markup=InlineKeyboardMarkup(RULES_BUTTON))

@bot.on_callback_query(filters.regex("Rules"))
async def rules(_, query: CallbackQuery):
    await query.edit_message_caption("""Oᴜʀ Sᴄᴀɴɴᴇʀ Rᴜʟᴇs Fᴏʀ Aʟʟ Oᴜʀ Tᴇʟᴇɢʀᴀᴍ Mᴇᴍʙᴇʀs""",
        reply_markup=InlineKeyboardMarkup(RULES_BUTTON2))
        
@bot.on_callback_query(filters.regex("basic_scanner_rules"))
async def basichelp(_, query: CallbackQuery):
    await query.edit_message_caption("""**Inspector Rules**

• `don't scan without reason to anyone`

• `don't scan Without Proof, scan With Correct Proof`

• `don't scan your personal issues`

• `don't scan first check the reason carefully` 

• `don't scan private chat because were don't trust private things`

• `don't give proof with clear pornography proof Hide and add reason`""",
        reply_markup=InlineKeyboardMarkup(RULES_BUTTON2))
        
@bot.on_callback_query(filters.regex("Girls_Safe_Rule"))
async def girlssafe(_, query: CallbackQuery):
    await query.edit_message_caption("""**Girls And Boys Safe Zone**

• `Don't Abuse Anyone, If You Abuse AnyOne Then You Will Get Ban From AnyOne`

• `Porn Girls And Gay Boys Are Not Allowed In Group`""",
        reply_markup=InlineKeyboardMarkup(RULES_BUTTON2))
        

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
        reply_markup=InlineKeyboardMarkup(RULES_BUTTON2))
        

@bot.on_callback_query(filters.regex("Toxic_Boom"))
async def basictoxirules(_, query: CallbackQuery):
    await query.edit_message_caption("""**Toxic Rules** 

• `Use Less Toxic For Your Entertainment`

• `Don't Use Unwanted`""",
        reply_markup=InlineKeyboardMarkup(RULES_BUTTON2))

        
