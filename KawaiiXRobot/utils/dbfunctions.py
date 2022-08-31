from KawaiiXRobot import mdb

gbansdb = mdb.gban

async def is_gbanned_user(user_id: int) -> bool:
    user = await gbansdb.find_one({"user_id": user_id})
    if not user:
        return False
    else:
        return True


async def add_gban_user(user_id: int):
    is_gbanned = await is_gbanned_user(user_id)
    if is_gbanned:
        return
    return await gbansdb.insert_one({"user_id": user_id})


async def remove_gban_user(user_id: int):
    is_gbanned = await is_gbanned_user(user_id)
    if not is_gbanned:
        return
    return await gbansdb.delete_one({"user_id": user_id})


async def get_gbans_count() -> int:
    return len([i async for i in gbansdb.find({"user_id": {"$gt": 0}})])

async def get_gbans_id() -> int:
    return str([i async for i in gbansdb.find({"user_id": {"$gt": 0}})])

async def get_gbans_data() -> int:
    async for i in gbansdb.find({"user_id": {"$gt": 0}})
          return str(i['user_id'])
