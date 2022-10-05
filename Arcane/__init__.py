import os
import time
from pyrogram import Client
from Arcane.utils.enfsdb import get_enfusers
from pymongo import MongoClient
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from Arcane.utils.db import DATABASE

# API_HASH & API_ID FOR UBOT
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION", None)
# APP_ID & APP_HASH FOR BOT
APP_ID = os.environ.get("APP_ID", None)
APP_HASH = os.environ.get("APP_HASH", None)
TOKEN = os.environ.get("TOKEN", None)
MONGO_URI = os.environ.get("MONGO_URI", None)
ARCANE_CHANNEL = os.environ.get("ARCANE_CHANNEL", None)
ARCANE_LOGS = os.environ.get("ARCANE_LOGS", None)
DEVS = [
 5696053228, 5446914371, 1989750989, 953362604
]
Inspector = [
 1544286112
]
Enforcer = [
 1057561033
]

async def Enforcer():
     list = (await get_enfusers())
     return list

PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]
MONGO_URL = "mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority"
mongo_client = MongoClient("mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority")
mdb = mongo_client.gof
db = DATABASE(MONGO_URI)
bot = Client("Arcane", api_id=APP_ID, api_hash=APP_HASH, bot_token=TOKEN)
ubot = Client(session_string=SESSION, api_id=API_ID, api_hash=API_HASH, name="ArcaneSystem") 
StartTime = time.time()

ubot.start()

print("I'M Back 👍")
