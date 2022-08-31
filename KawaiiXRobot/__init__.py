import os
import time
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from KawaiiXRobot.utils.db import DATABASE
StartTime = time.time()

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
MONGO_URI = os.environ.get("MONGO_URI", None)
KAWAII_LOGS = os.environ.get("KAWAII_LOGS", None)
KAWAII_CHANNEL = os.environ.get("KAWAII_CHANNEL", None)
DEVS = os.environ.get("DEVS", None)
Inspector = os.environ.get("Inspector", None)
Enforcer = os.environ.get("Enforcer", None)

DEVS = [
 5175767264, 1989750989, 1544286112, 1491497760
]
Inspector = [
 1057561033
]
Enforcer = [
 1891633746, 5446914371
]


bot = Client("cringe_X_Robot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db = DATABASE(MONGO_URI)
mongo_client = MongoClient("mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority")
mdb = mongo_client.gof

print("Starting The Cringe X System")
