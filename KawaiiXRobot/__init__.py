import os
import time
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from Cringe.utils.db import DATABASE
StartTime = time.time()

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
MONGO_URI = os.environ.get("MONGO_URI", None)
CRINGE_LOGS = os.environ.get("CRINGE_LOGS", None)
CRINGE_CHANNEL = os.environ.get("CRINGE_CHANNEL", None)
DEVS = [
 5175767264, 1989750989, 5251017390
]
CRINGE_GUYS = [
 1057561033, 5163504846, 
]
CRINGE_KID = [
 1891633746, 5145883564
]
bot = Client("CringeGuys", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))
db = DATABASE(MONGO_URI)
mongo_client = MongoClient("mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority")
mdb = mongo_client.gof

print("Starting The Cringe X System")
