from Arcane.utils.dbfunctions import get_enforcers
from Arcane.utils.dbfunctions import get_Inspector

async def Enforcers():
     list = (await get_enforcers())
     return list

async def Inspector():
     list = (await get_Inspector())
     return list

