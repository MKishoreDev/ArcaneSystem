import os
import time
from pyrogram import Client
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from KawaiiXRobot.utils.db import DATABASE

from telethon import TelegramClient
from telethon.sessions import MemorySession

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
MONGO_URI = os.environ.get("MONGO_URI", None)
KAWAII_LOGS = os.environ.get("KAWAII_LOGS", None)
KAWAII_CHANNEL = os.environ.get("KAWAII_CHANNEL", None)
DEVS = os.environ.get("DEVS", None)
Inspector = os.environ.get("Inspector", None)
Enforcer = os.environ.get("Enforcer", None)
PYRO_SESSION = "BQDqqZsAGsT3prxh157M2aPeX6Za0vgOOlDVPFyv-_Sf9nTXAhj1JR7567Ts59ZV3f7e-CLCwKqbIJFYzoprzXinPprx93_gJNK3OgCIaBD2tj-KIa1M_zHa6tB3PwoaInDVUfLDfMd3igOkBk-l08DsvG1WbiCYyIsQxEM8clyZiJU0vVXBhfKJ-Lsg7_7YJJD5mPAZwIVbUcmr3Mlan-YW42vp1Aet8D4WaS1W9EOq57r7NRY-mUGZwrdiRaz7coETfyCssIhriZWkHdzntAwZI8uQAIDuuHET4Y59OyuH7ed82HoJ5u_n4AUBnCuqDi1yeWRy0LJGtL_cHFGeLtKD_tio-gAAAAFCPvD-AA"                            
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
tbot = TelegramClient(MemorySession(), API_ID, API_HASH)

StartTime = time.time()
ubot.start()
tbot.start(bot_token=BOT_TOKEN)

print("Starting The Cringe X System")
