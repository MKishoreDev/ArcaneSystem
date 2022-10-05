# Dev.py ©Copyright By @ProErrorDxD  Machan

import time
from Arcane import bot as app
from Arcane import bot, DEVS, PREFIX
from Arcane import StartTime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import sys, traceback, io
from subprocess import getoutput as run
from requests import get, post

def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

@app.on_message(filters.command("eval", PREFIX))
async def eval(client, message):
    if message.from_user.id in DEVS:

        status_message = await message.reply_text("Processing ...")
        cmd = message.text.split(" ", maxsplit=1)[1]

        reply_to_ = message
        if message.reply_to_message:
            reply_to_ = message.reply_to_message

        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None

        try:
            await aexec(cmd, client, message)
        except Exception:
            exc = traceback.format_exc()

        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr

        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"

        final_output = "<b>EVAL</b>: "
        final_output += f"<code>{cmd}</code>\n\n"
        final_output += "<b>OUTPUT</b>:\n"
        final_output += f"<code>{evaluation.strip()}</code> \n"

        if len(final_output) > 4096:
            with io.BytesIO(str.encode(final_output)) as out_file:
                out_file.name = "eval.text"
                await reply_to_.reply_document(document=out_file,
                                               caption=cmd,
                                               disable_notification=True)
        else:
            await reply_to_.reply_text(final_output)
        await status_message.delete()

    else:
        await message.reply("This Is A kawaii User's Restricted Command.You Don't Have Access To Use This.")


async def aexec(code, client, message):
    exec("async def __aexec(client, message): " +
         "".join(f"\n {l_}" for l_ in code.split("\n")))
    return await locals()["__aexec"](client, message)


@app.on_message(filters.command("sh", PREFIX))
def sh(_, m):
    if m.from_user.id in DEVS:
        code = m.text.replace(m.text.split(" ")[0], "")
        x = run(code)
        m.reply(
            f"<b>SHELL</b>: <code>{code}</code>\n\n<b>OUTPUT</b>:\n<code>{x}</code>")
    else:
        m.reply("This Is A Kawaii User's Restricted Command.You Don't Have Access To Use This.")

@bot.on_message(
    filters.command("logs", prefixes=['.', '/', ';', ','
                                      '*']) & filters.user(DEVS))
def sendlogs(_, m: Message):
    logs = run("tail logs.txt")
    x = paste(logs)
    keyb = [
        [
            InlineKeyboardButton("Link", url=x),
            InlineKeyboardButton("File", callback_data="sendfile")
        ],
    ]
    m.reply(x,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(keyb))


@bot.on_callback_query(filters.regex(r"sendfile"))
def sendfilecallback(_, query: CallbackQuery):
    sender = query.from_user.id
    chat = query.message.chat.id

    if sender in DEVS:
        query.message.edit("`Sending...`")
        query.message.reply_document("logs.txt")

    else:
        query.answer("This Is A Arcane User's Restricted Command.You Don't Have Access To Use This.")

