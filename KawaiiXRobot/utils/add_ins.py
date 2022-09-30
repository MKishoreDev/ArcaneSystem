import codecs
import pickle
from typing import Dict, List, Union

from KawaiiXRobot import mdb

Inspectordb = mdb.Inspector

async def get_Inspector() -> list:
    Inspector = await Inspectordb.find_one({"Inspector": "Inspector"})
    if not Inspector:
        return []
    return Inspector["Inspector"]


async def add_Inspector(user_id: int) -> bool:
    Inspector = await get_Inspector()
    Inspector.append(user_id)
    await Inspectordb.update_one(
        {"Inspector": "Inspector"}, {"$set": {"Inspector": Inspector}}, upsert=True
    )
    return True


async def remove_Inspector(user_id: int) -> bool:
    Inspector = await get_sudoers()
    Inspector.remove(user_id)
    await Inspectordb.update_one(
        {"Inspector": "Inspector"}, {"$set": {"Inspector": Inspector}}, upsert=True
    )
    return True
