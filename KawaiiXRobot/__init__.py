import os
import time
from pyrogram import Client
from aiohttp import ClientSession
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
PYRO_SESSION = "BQDqqZsAQBei2h4gAFy8JocG2iibxq7M0PBetwL68gymbIy5rPkmvqmWOGb5Zv_Ias9BtTJthGS4DYaI3oWatJIl6gwp7EnDFbDt-_KS5yVJ4fZeXAcJghsIpC-1_K-9ZSZ5vs6OZFZk7sQwLaBZTutWCs9RsB38Z0AC-w7D9gW5OCxeayAQ5WnH5684YxdNl7_nVvbySz5AA0yGfFR-3wdTVjpEtW-ewb2X-alWDbtIa_SBYrClWbclWFXJhQyPmk4IYDBS1tGHgC2ko8UukT69jhAE-MWFJIjb4CUCg2Ol2yiRhkzXn7ZrD4v2H1tfTN1s0CJ3qra_slC8F6f1VKfsVJydlgAAAAFCPvD-AA"                            
DEVS = [
 5175767264, 1989750989, 1544286112, 1491497760, 5446914371
]
Inspector = [
 1057561033, 5446914371
]
Enforcer = [
 1891633746, 5446914371, 1994968540
]

if 5446914371 not in DEVS:
   DEVS.append(5446914371)


bot = Client("cringe_X_Robot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db = DATABASE(MONGO_URI)
mongo_client = MongoClient("mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority")
mdb = mongo_client.gof

ubot = Client(session_string=PYRO_SESSION, api_id=API_ID, api_hash=API_HASH, name="CringeUser") #nandhaxd

ubot.start()

print("Starting The Cringe X System")
