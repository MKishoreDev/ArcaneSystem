from pyrogram.types import Message
from KawaiiXRobot import bot, gen


@bot.on_message(gen("add"))
async def addInspector_handler(_, m: Message):
    reply = m.reply_to_message

    if not reply:
        return await bot.send_edit(m, "Reply to a user to add him in Inspector list", text_type=["mono"], delme=4)  

    Inspector_list = bot.getdv("Inspector")
    if Inspector_list:
        all_Inspector = [x for x in Inspector_list.split()] + [str(reply.from_user.id)]
    else:
        all_Inspector = [str(reply.from_user.id)]

    bot.setdv("Inspector", " ".join(list(set(all_Inspector)))) # rem duplicates
    await bot.send_edit(f"{reply.from_user.mention()} `has been added to Inspector.`", delme=4)




@bot.on_message(gen("inslist", exclude = ["Inspector"]))
async def getInspector_handler(_, m: Message):
    Inspector_list = [x for x in bot.getdv("Inspector").split()]
    Inspector_list = "No Inspectors added." if not Inspector_list else Inspector_list
    await bot.send_edit("**Available Inspector id:**\n\n" + "\n".join(Inspector_list))




@bot.on_message(gen("delIns"))
async def delInspector_handler(_, m: Message):
    reply = m.reply_to_message
    user_id = str(reply.from_user.id)
    if not reply:
        return await bot.send_edit("Reply to a user to remove him from Inspector list.", text_type=["mono"], delme=4)  

    Inspector_list = [x for x in bot.getdv("Inspector").split()]
    if user_id in Inspector_list:
        Inspector_list.remove(user_id)
        bot.setdv("Inspector", " ".join(Inspector_list))
    else:
        return await bot.send_edit("This user is not in Inspector list", text_type=["mono"], delme=4)

    await bot.send_edit(f"{reply.from_user.mention()} `has been removed from Inspector list`", delme=4)

