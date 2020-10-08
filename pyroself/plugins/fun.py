import time, requests, os, urllib
from pyrogram import Client, Filters, __version__
from pyroself import COMMAND_HAND_LER
from pyrogram.api.all import layer
from pyroself.utils.sendmsg import sendmsg
__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

__help__ = f"""
راهنمای بخش فان

دریافت عکس کون
`{COMMAND_HAND_LER}kon`
دریافت عکس ممه
`{COMMAND_HAND_LER}mme`
"""

@Client.on_message(Filters.command("kon","") & Filters.me)
async def kon(client, message):
    await message.delete()
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), "*.jpg")
    os.rename("*.jpg", "kon.jpg")
    await client.send_photo(message.chat.id, "kon.jpg")
    os.remove("kon.jpg")

@Client.on_message(Filters.command("mme","") & Filters.me)
async def mme(client, message):
    await message.delete()
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), "*.jpg")
    os.rename("*.jpg", "mme.jpg")
    await client.send_photo(message.chat.id, "mme.jpg")
    os.remove("mme.jpg")