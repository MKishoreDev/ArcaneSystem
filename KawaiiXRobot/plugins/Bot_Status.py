# © Copyright By @DeepakJackson

import os
import pytz
import asyncio
import datetime
from KawaiiXRobot bot, ubot
from config import import DEVS, Inspector, MESSAGE_ID, CHANNEL_OR_GROUP_ID, BOT_LIST, TIME_ZONE
from pyrogram import filters, Client
from pyrogram.errors import FloodWait

async def statusbots():
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
                        

