from KawaiiXRobot import bot
from KawaiiXRobot.plugins import ALL_MODULES
import logging
import glob
import asyncio
import importlib
import sys
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"KawaiiXRobot/plugins/{plugin_name}.py")
    name = "KawaiiXRobot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["KawaiiXRobot.plugins." + plugin_name] = load
    print("Total Plugins -->" + ALL_MODULES)
    print("Imported --> " + plugin_name)

path = "KawaiiXRobot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        thepath = Path(a.name)
        plugin_name = thepath.stem
        load_plugins(plugin_name.replace(".py", ""))

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)

def main():
    bot.run()

if __name__ == "__main__":
     main()
   
