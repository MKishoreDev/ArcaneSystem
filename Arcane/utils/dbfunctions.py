from Arcane import mdb

gbansdb = mdb.gban
ranksdb = mdb.rankuserdb

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





async def get_rankusers() -> list:
    rank_users = await ranksdb.find_one({"user_id": "user_id"})
    if not rank_users:
        return []
    return rank_users["rank_users"]

async def add_rank(user_id: int):
      rank_users = await get_rankusers()
      rank_users.append(user_id)
      await ranksdb.update_one(
        {"user_id": "user_id"}, {"$set": {"rank_users": rank_users}}, upsert=True)
      return True  

async def remove_rank(user_id: int):
       rank_users = await get_rankusers()
       rank_users.remove(user_id)
       await ranksdb.update_one(
        {"user_id": "user_id"}, {"$set": {"rank_users": rank_users}}, upsert=True)
       return True
