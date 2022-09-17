# __main__.py ©Copyright By @ProErrorDxD  Machan

from KawaiiXRobot import bot, ubot
import os
import pytz
import datetime
import logging
import glob
import asyncio
import importlib
import sys
from pathlib import Path
from config import DEVS, Inspector, MESSAGE_ID, CHANNEL_OR_GROUP_ID, BOT_LIST, TIME_ZONE
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
            
def load_plugins(plugin_name):
    punda = "KawaiiXRobot/plugins/*.py"
    devu = f"{len(glob.glob(punda))}"
    path = Path(f"KawaiiXRobot/plugins/{plugin_name}.py")
    name = "KawaiiXRobot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["KawaiiXRobot.plugins." + plugin_name] = load
    print("Total Plugins -->" + devu)
    print("Imported --> " + plugin_name)

path = "KawaiiXRobot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        thepath = Path(a.name)
        plugin_name = thepath.stem
        shit = plugin_name.replace(".py", "")
        load_plugins(shit)

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)

async def main():
    async with ubot:
            while True:
                GET_CHANNEL_OR_GROUP = await ubot.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                checker_bot = f"💡 **<u>LIVE BOT STATUS</u>** 💡\n\n💬 **{CHANNEL_OR_GROUP_NAME}**"
                for bot in BOT_LIST:
                    try:
                        checker_status = await ubot.send_message(bot, "/Sbot")
                        aaa = checker_status.message_id
                        await asyncio.sleep(10)
                        checker_user = await ubot.get_history(bot, limit = 1)
                        for ccc in checker_user:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            checker_bot += f"\n\n🤖 **BOT**: @{bot}\n🔴 **STATUS**: down ❌"
                            for bot_admin_id in DEVS:
                                try:
                                    await ubot.send_message(int(bot_admin_id), f"🚨 **announcement** 🚨\n\n» @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await ubot.read_history(bot)
                        else:
                            checker_bot += f"\n\n🤖 **BOT**: @{bot}\n🟢 **STATUS**: alive ✅"
                            await ubot.read_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                checker_bot += f"\n\n🛂 Last Check: {last_update} ({TIME_ZONE})\n\n🟡 **updates every 45 min(s)**\n\n⚡ Powered by:- @Cringe_X_NetWork"
                await ubot.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, checker_bot)               
                await asyncio.sleep(2700)

if __name__ == "__main__":
     bot.run()
     ubot.run()
     main()
   
