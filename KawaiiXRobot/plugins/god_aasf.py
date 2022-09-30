from KawaiiXRobot import DEVS, bot
from KawaiiXRobot.utils.adddb import add_enf, rm_enf, enf_list
from pyrogram import filters
from pyrogram.errors import RPCError

text = "Enforcers List:"


@bot.on_message(filters.command("addenf"))
async def add_enf(_, message):
	chat_id = message.chat.id
	if message.reply_to_message:
		user_id = message.reply_to_message.from_user.id
		mention = message.reply_to_message.from_user.mention
	else:
		args = message.text.split(None,2)
		try:
			user = await bot.get_users(args[1])
			user_id = user.id
			mention = user.mention
		except RPCError:
			await message.reply_text("`User Not Found`")
			return
	await add_enf(user_id)
	await message.reply_photo("https://telegra.ph/file/c2bbc8ce37d490a182330.jpg", caption=f"Successfully Added {mention} To Enforcer")

@bot.on_message(filters.command("rmenf"))
async def rm_enf(_, message):
	chat_id = message.chat.id
	if message.reply_to_message:
		user_id = message.reply_to_message.from_user.id
		mention = message.reply_to_message.from_user.mention
	else:
		args = message.text.split(None,2)
		try:
			user = await bot.get_users(args[1])
			user_id = user.id
			mention = user.mention
		except RPCError:
			await message.reply_text("`User Not Found`")
			return

	await rm_enf(user_id)
	await message.reply_text("Successfully Removed User From Enf")

@bot.on_message(filters.command("enflist"))
async def enflist(_, message):
	chat_id = message.chat.id
	enf_list = await enf_list()
	for enf in enf_list:
		user = await bot.get_users(enf.user_id)
		mention = user.mention
		text += "\n - {}".format(mention)
	await message.reply_text(text)
