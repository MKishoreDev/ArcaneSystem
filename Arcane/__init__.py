import time

from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

API_ID = "15378843"
API_HASH = "03e07e4821f7cfd77018a04196550e4b"
TOKEN = "5620916588:AAF9O_cVQ8rrlj-JZoqpjPCEaDjCPpMONrY"
DEVS = [
 5696053228, 5446914371, 1544286112, 1989750989
]

MONGO_URL = "mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority"
SESSION = ""

bot = Client("Arcane", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
ubot = Client(session_string=SESSION, api_id=API_ID, api_hash=API_HASH, name="ArcaneSystem") 
mongo_client = MongoClient(MONGO_URL)
StartTime = time.time()
