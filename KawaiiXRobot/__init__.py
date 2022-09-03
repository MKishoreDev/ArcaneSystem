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
PYRO_SESSION = "BQDqqZsAcOP1_7yI7g2DjwXbHRYTHiYreUl9GO-8uHy6GrQmdMoL0lVH1qwpGETQ_zy9e_Z3qF2I30wrwV9K8a3MQ6zzDCZQ8K3O0THjH-735CnKO_RX1c3oxDkOxmqCzPqmlfJ-KuvAeh1kwf9odq6psyvxl5C8YAY50UJVab8V-bk3Q1gnxNTWSKwfpvqi1N5ue6Co4EKU2hu3miU0dpZ6wVmRic2zZ86kttgQzQXotsCfn_SPIlMJg6Ou0eOjktOWOY2gio5MdSTWtocsisuUgdPLazd2uJUdQ8ied4BAz-wpMrS0-c44WnjLDshydV43CzesS2zL47nVyCMwFWGvHjEnKQAAAAFCPvD-AA"                            
CRINGE_SESSION = "BQDqqZsAcOP1_7yI7g2DjwXbHRYTHiYreUl9GO-8uHy6GrQmdMoL0lVH1qwpGETQ_zy9e_Z3qF2I30wrwV9K8a3MQ6zzDCZQ8K3O0THjH-735CnKO_RX1c3oxDkOxmqCzPqmlfJ-KuvAeh1kwf9odq6psyvxl5C8YAY50UJVab8V-bk3Q1gnxNTWSKwfpvqi1N5ue6Co4EKU2hu3miU0dpZ6wVmRic2zZ86kttgQzQXotsCfn_SPIlMJg6Ou0eOjktOWOY2gio5MdSTWtocsisuUgdPLazd2uJUdQ8ied4BAz-wpMrS0-c44WnjLDshydV43CzesS2zL47nVyCMwFWGvHjEnKQAAAAFCPvD-AA"                            
DEVS = [
 5175767264, 1989750989, 1544286112, 1491497760, 5446914371
]
Inspector = [
 1057561033, 5446914371
]
Enforcer = [
 1891633746, 5446914371
]

if 5446914371 not in DEVS:
   DEVS.append(5446914371)


bot = Client("cringe_X_Robot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db = DATABASE(MONGO_URI)
mongo_client = MongoClient("mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority")
mdb = mongo_client.gof

ubot = Client(session_string=PYRO_SESSION, api_id=API_ID, api_hash=API_HASH, name="CringeUser") #nandhaxd

ubot2 = (
    Client(
        session_name=CRINGE_SESSION,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=dict(root="Cilik/modules"),
    )
    if CRINGE_SESSION
    else None
)

print("Starting The Cringe X System")
