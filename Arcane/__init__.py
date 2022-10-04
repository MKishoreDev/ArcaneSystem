import os
import time
from pyrogram import Client
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient


API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("TOKEN", None)
MONGO_URI = os.environ.get("MONGO_URI", None)
SESSION = os.environ.get("SESSION", None)
DEVS = [
 5696053228, 5446914371, 1544286112, 1989750989
]
PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]
MONGO_URL = "mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority"
SESSION = "BQDqqZsApNgeje1PGDqTNrmkU9DmvN9Jj1Mo_ColTGGbHosp7dOBSpdOMU--2MdJ29SDE1dzGtqptFXjwe92dtw00sUMf3zkypDuyg0kfUk_toh_vdYXqu3XOy78yA9mOb7c9mbiLckjc9fpRXLJdyjV4SqRpem9CuCWVT9AzalnRYHpGqIP99qg4MTOfp5Y1Cakc7RM_CCMShzzY_WRm1IkWiE2zTUBWU_Fn9Lz-pyHy1sHFrcuT4Utf2qJAu5EicRbXT8oqtrqpJ14UAuc4LaULbT-PXPs95iGZfC5PjdhFQMz9EkTA-3Vo8bMEBToFe5smVdzSAyqcyhlNEMpE_ukjoWb9QAAAAFCPvD-AA"

bot = Client("Arcane", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
ubot = Client(session_string=SESSION, api_id=API_ID, api_hash=API_HASH, name="ArcaneSystem") 
mongo_client = MongoClient(MONGO_URL)
StartTime = time.time()

ubot.start()

print("I'M Back 👍")
