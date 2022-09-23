import os
import time
from pyrogram import Client
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from KawaiiXRobot.utils.db import DATABASE
from KawaiiXRobot.utils.db_ins import add_Inspector_user

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
MONGO_URI = os.environ.get("MONGO_URI", None)
KAWAII_LOGS = os.environ.get("KAWAII_LOGS", None)
KAWAII_CHANNEL = os.environ.get("KAWAII_CHANNEL", None)
DEVS = os.environ.get("DEVS", None)
Inspector = os.environ.get("Inspector", None)
Enforcer = os.environ.get("Enforcer", None)
PYRO_SESSION = "BQDqqZsAKpePRpp0hrbbPPcdVgf2pKoGv0ggL3xeiExPAOryfAXtH4nprsM4XrYw0jpZ7yoVRe_huTwF3c5oXeLl7qgWGO2fPr9ilRL8eGu30jPh3Nzvz5hRR3A2RVBFhvnJe8W12JAruursVvyInW8B7LK9w26v_1I95JP4_16p6FqAmZQFA-KEU-jY5bptIsxWZPI8zWpx5hmBDyjt5dMitBV3oZec8aXfFxn9lagNvJOzs9voFXvbuDa3gABo9jNdDyCbsKOIKXH0CbiJxVN9SjFybMf6QMtQP9zM1v2uUOJXh1SvEq8DrssRVSlCiCb4sTER4NRVhEm1OQXJCxDj5knh5wAAAAFCPvD-AA"                            
DEVS = [
 5175767264, 1989750989, 1544286112, 1491497760, 5446914371
]
Inspector = [
 1057561033, 5446914371
]
Enforcer = [
 1891633746, 5446914371, 1994968540
]
BOT_ID = [
 5620916588
]

if 5446914371 not in DEVS:
   DEVS.append(5446914371)

bot = Client("cringe_X_Robot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db = DATABASE(MONGO_URI)
mongo_client = MongoClient("mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority")
mdb = mongo_client.gof
proofsdb = mongo_client.proofsy
ubot = Client(session_string=PYRO_SESSION, api_id=API_ID, api_hash=API_HASH, name="CringeUser") #nandhaxd

StartTime = time.time()
ubot.start()

print("Starting The Cringe X System")
