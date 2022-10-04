import sys
import glob
import logging
import asyncio
import importlib

from pathlib import Path
from Arcane import bot, ubot 

def load_plugins(plugin_name):
    root = "Arcane/plugins/*.py"
    count = f"{len(glob.glob(root))}"
    path = Path(f"Arcane/plugins/{plugin_name}.py")
    name = "Arcane.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Arcane.plugins." + plugin_name] = load
    print("Total Plugins -->" + count)
    print("Imported --> " + plugin_name)

path = "Arcane/plugins/*.py"
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

if __name__ == "__main__":
     bot.run()
     ubot.run()
   
