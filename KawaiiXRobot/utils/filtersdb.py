from KawaiiXRobot import db, bot
from typing import Dict, List, Union


proofsdb = db.proofs

async def get_proofs_count() -> dict:
    proofs_count = 0
    async for x in proofsdb.find({"proofs_id": {"$lt": 0}}):
        proofs_name = await get_proof_names(x["proofs_id"])
        proofs_count += len(proofs_name)
    return {
        "proofs_count": proofs_count,
    }


async def _get_proofs(proofs_id: int) -> Dict[str, int]:
    _proofs = await proofsdb.find_one({"proofs_id": proofs_id})
    if not _proofs:
        return {}
    return _proofs["proofs"]


async def get_proof_names(proofs_id: int) -> List[str]:
    _proofs = []
    for _proof in await _get_proofs(proofs_id):
        _proofs.append(_proof)
    return _proofs


async def get_proof(proofs_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _proofs = await _get_proofs(proofs_id)
    if name in _proofs:
        return _proofs[name]
    return False


async def save_proof(proofs_id: int, name: str, _proof: dict):
    name = name.lower().strip()
    _proofs = await _get_proofs(proofs_id)
    _proofs[name] = _proof
    await proofsdb.update_one(
        {"proofs_id": proofs_id},
        {"$set": {"proofs": _proofs}},
        upsert=True,
    )


async def remove_proof(proofs_id: int, name: str) -> bool:
    proofsd = await _get_proofs()
    name = name.lower().strip()
    if name in proofsd:
        del proofsd[name]
        await proofsdb.update_one(
            {"proofs_id": proofs_id},
            {"$set": {"proofs": proofsd}},
            upsert=True,
        )
        return True
    return False
