import time
import os
from pyrogram import Client, Filters, __version__
from pyroself import COMMAND_HAND_LER
from pyrogram.api.all import layer
from pyroself.utils.sendmsg import sendmsg
from pyroself.utils.database import db
__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

__help__ = f"""
"""


@Client.on_message(Filters.private)
async def monshi(client, message):
	try:
		me = await client.get_me()
		status = me.status
		monshi_mode = db.get("monshi-mode")
		if status == "offline":
			if monshi_mode == "on":
				txt = db.get('monshi:text') or "دوست عزیز الان افلاینم منتظر بمون تا انلاین بشم جواب میدم!"
				await client.send_message(message.chat.id, txt)
			else:
				pass
		else:
			pass
	except:
		print("eror code monshi!")


@Client.on_message(Filters.me & Filters.regex("^[Ss]ettext (.*)$"))
async def monshi_text(client, message):
    txt = message.text.split(" ")[1:50]
    text = " "
    text = text.join(txt)
    db.set("monshi:text" , text)
    await message.edit(f"متن زیر با موفقیت ثبت شد! \n متن منشی : <u>{text}</n>")


@Client.on_message(Filters.me & Filters.regex("^[Mm]onshi$"))
async def monshi_mode(client, message):
    if db.get("monshi-mode") == "on":
        db.set("monshi-mode","off")
        txt = f"**حالت منشی سلف غیرفعال شد**"
    else:
        db.set("monshi-mode","on")
        txt = f"**حالت منشی سلف فعال شد**"
    await message.edit(txt)