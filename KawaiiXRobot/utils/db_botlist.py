from KawaiiXRobot import mdb

botsdb = mdb.gban

async def is_Boted_user(user_id: int) -> bool:
    user = await botsdb.find_one({"user_id": user_id})
    if not user:
        return False
    else:
        return True


async def add_gban_user(user_id: int):
    is_Boted = await is_Boted_user(user_id)
    if is_Boted:
        return
    return await botsdb.insert_one({"user_id": user_id})


async def remove_gban_user(user_id: int):
    is_Boted = await is_Boted_user(user_id)
    if not is_Boted:
        return
    return await botsdb.delete_one({"user_id": user_id})


async def get_bots_count() -> int:
    return len([i async for i in botsdb.find({"user_id": {"$gt": 0}})])

async def get_bots_id() -> int:
    return str([i async for i in botsdb.find({"user_id": {"$gt": 0}})])

async def get_bots_data() -> int:
    return ([i['user_id'] async for i in botsdb.find({"user_id": {"$gt": 0}})])
