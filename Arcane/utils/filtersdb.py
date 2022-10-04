from Arcane import proofsdb, bot
from typing import Dict, List, Union


async def get_proofs_count() -> dict:
    proofs_count = 0
    async for x in proofsdb.find({"proofs_id": {"$lt": 0}}):
        proofs_name = await get_proof_names(x["proofs_id"])
        proofs_count += len(proofs_name)
    return {
        "proofs_count": proofs_count,
    }


async def _get_proofs() -> Dict[str, int]:
    _proofs = await proofsdb.find_one({"proofs_id"})
    if not _proofs:
        return {}
    return _proofs["proofs"]


async def get_proof_names() -> List[str]:
    _proofs = []
    for _proof in await _get_proofs():
        _proofs.append(_proof)
    return _proofs


async def get_proof(proofs_id: str) -> Union[bool, dict]:
    name = proofs_id.lower().strip()
    _proofs = await _get_proofs()
    if name in _proofs:
        return _proofs[name]
    return False


async def save_proof(proofs_id: str, _proof: dict):
    name = proofs_id.lower().strip()
    _proofs = await _get_proofs(proofs_id)
    _proofs[name] = _proof
    await proofsdb.update_one(
        {"proofs_id": proofs_id},
        {"$set": {"proofs": _proofs}},
        upsert=True,
    )


async def remove_proof(proofs_id: str) -> bool:
    proofsd = await _get_proofs()
    name = proofs_id.lower().strip()
    if name in proofsd:
        del proofsd[name]
        await proofsdb.update_one(
            {"proofs_id": proofs_id},
            {"$set": {"proofs": proofsd}},
            upsert=True,
        )
        return True
    return False
