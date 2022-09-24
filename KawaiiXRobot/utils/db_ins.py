from KawaiiXRobot.utils import mdb

Inspectordb = mdb.Inspector

async def is_Inspector_user(user_id: int) -> bool:
    user = await Inspectordb.find_one({"user_id": user_id})
    if not user:
        return False
    else:
        return True


async def add_Inspector_user(user_id: int):
    is_Inspector = await is_Inspector_user(user_id)
    if is_Inspector:
        return
    return await Inspectordb.insert_one({"user_id": user_id})


async def remove_Inspector_user(user_id: int):
    is_Inspector = await is_Inspector_user(user_id)
    if not is_Inspector:
        return
    return await Inspectordb.delete_one({"user_id": user_id})


async def get_Inspector_count() -> int:
    return len([i async for i in Inspectordb.find({"user_id": {"$gt": 0}})])

async def get_Inspector_id() -> int:
    return str([i async for i in Inspectordb.find({"user_id": {"$gt": 0}})])

async def get_Inspector_data() -> int:
    return ([i['user_id'] async for i in Inspectordb.find({"user_id": {"$gt": 0}})])
