from Arcane import mdb

gbansdb = mdb.gban
enforcersdb = mdb.enforcersdb

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
    return ([i['user_id'] async for i in gbansdb.find({"user_id": {"$gt": 0}})])





async def get_enforcers() -> list:
    enforcers = await enforcersdb.find_one({"user_id": "user_id"})
    if not enforcers:
        return []
    return enforcers["enforcers"]

async def add_enforcers(user_id: int):
      enforcers = await get_enforcers()
      enforcers.append(user_id)
      await enforcersdb.update_one(
        {"user_id": "user_id"}, {"$set": {"enforcers": enforcers}}, upsert=True)
      return True  

async def remove_enforcers(user_id: int):
       enforcers = await get_enforcers()
       enforcers.remove(user_id)
       await enforcersdb.update_one(
        {"user_id": "user_id"}, {"$set": {"enforcers": enforcers}}, upsert=True)
       return True
