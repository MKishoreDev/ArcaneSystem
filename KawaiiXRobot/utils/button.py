import re
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)]\(buttonurl:/{0,2}(.+?)(:same)?\))")

def get_keyboard(data):
  if len([match for match in BTN_URL_REGEX.finditer(data)]) == 0:
    return data, None
  else:
    cont = data.split([match for match in BTN_URL_REGEX.finditer(data)][0].group(1), 1)[0]
    if [match for match in BTN_URL_REGEX.finditer(data)][0].group(1) in cont:
      cont = None
    lis = []
    for match in BTN_URL_REGEX.finditer(data):
      but = []
      if bool(match.group(4)):
        lis[-1].append(InlineKeyboardButton(text=match.group(2), url=match.group(3)))
      else:
        but.append(InlineKeyboardButton(text=match.group(2), url=match.group(3)))
      if len(but) != 0:
        lis.append(but)
    if len(lis) != 0:
      return cont, InlineKeyboardMarkup(lis)
    else:
      return cont, None
