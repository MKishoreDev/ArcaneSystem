from Arcane import mdb

enfdb = mdb.enf

async def is_enf(user_id: int) -> bool:
    user = await enfdb.find_one({"user_id": user_id})
    if not user:
        return False
    else:
        return True


async def add_enf(user_id: int):
    is_enf_user = await is_enf(user_id)
    if is_enf_user:
        return
    return await enfdb.insert_one({"user_id": user_id})


async def rm_enf(user_id: int):
    is_enf_user = await is_enf(user_id)
    if not is_enf_user:
        return
    return await enfdb.delete_one({"user_id": user_id})


async def  enf_list_count() -> int:
    return len([i async for i in enfdb.find({"user_id": {"$gt": 0}})])

async def enf_list() -> int:
    return  str([i async for i in enfdb.find({"user_id": {"$gt": 0}})])

async def enf_list_data() -> int:
    return ([i['user_id'] async for i in enfdb.find({"user_id": {"$gt": 0}})])
