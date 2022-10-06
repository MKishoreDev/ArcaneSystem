from Arcane.utils.dbfunctions import get_enforcers

async def Enforcers():
     list = (await get_enforcers())
     return list
