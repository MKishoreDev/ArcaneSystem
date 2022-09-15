from KawaiiXRobot.utils.filtersdb import cli

filter = cli["Cringe"]["FILTER"]

async def save_proof(keyword, chat_id, message_id) -> None:
    add = await filter.find_one({"keyword": keyword})
    if add:
        await filter.update_one(
            {"keyword": keyword},
            {"$set": {"chat_id": chat_id, "msg_id": message_id}},
        )
    else:
        await filter.insert_one(
            {"keyword": keyword, "chat_id": chat_id, "msg_id": message_id}
        )


async def remove_proof(keyword, chat_id):
    await filter.delete_one({"keyword": keyword, "chat_id": chat_id})


async def get_proof(keyword, chat_id):
    r = await filter.find_one({"keyword": keyword, "chat_id": chat_id})
    if r:
        return r
    else:
        return False


async def remove_proof(chat_id):
    await filter.delete_many({"chat_id": chat_id})


async def get_proof_names(chat_id):
    r = [jo async for jo in filter.find({"chat_id": chat_id})]
    if r:
        return r
    else:
        return False
