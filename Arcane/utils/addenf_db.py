from Arcane import mdb

enfdb = mdb.enfuserdb

async def get_enfusers() -> list:
    enf_users = await enfsdb.find_one({"user_id": "user_id"})
    if not enf_users:
        return []
    return enf_users["enf_users"]
async def add_enf(user_id: int):
      enf_users = await get_enfusers()
      enf_users.append(user_id)
      await enfsdb.update_one(
        {"user_id": "user_id"}, {"$set": {"enf_users": enf_users}}, upsert=True)
      return True  
async def remove_enf(user_id: int):
       enf_users = await get_enfusers()
       enf_users.remove(user_id)
       await enfsdb.update_one(
        {"user_id": "user_id"}, {"$set": {"enf_users": enf_users}}, upsert=True)
       return True
