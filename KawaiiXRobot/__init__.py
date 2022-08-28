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
DEVS = [
 5175767264, 1989750989, 1491497760
]
KAWAII_A_RANK = [
 1057561033, 5163504846, 1491497760
]
KAWAII_B_RANK = [
 1891633746, 5163504846, 1491497760
]
bot = Client("KawaiiXRobot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))
db = DATABASE(MONGO_URI)
mongo_client = MongoClient("mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority")
mdb = mongo_client.gof

print("Starting The Kawaii X System")
