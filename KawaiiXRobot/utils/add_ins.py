from KawaiiXRobot import mdb
from typing import Dict, List, Union

inspectorersdb = mdb.inspectorers

async def get_inspectorers() -> list:
    inspectorers = await inspectorersdb.find_one({"inspector": "inspector"})
    if not inspectorers:
        return []
    return inspectorers["inspectorers"]


async def add_inspector(user_id: int) -> bool:
    inspectorers = await get_inspectorers()
    inspectorers.append(user_id)
    await inspectorersdb.update_one(
        {"inspector": "inspector"}, {"$set": {"inspectorers": inspectorers}}, upsert=True
    )
    return True


async def remove_inspector(user_id: int) -> bool:
    inspectorers = await get_inspectorers()
    inspectorers.remove(user_id)
    await inspectorersdb.update_one(
        {"inspector": "inspector"}, {"$set": {"inspectorers": inspectorers}}, upsert=True
    )
    return True

