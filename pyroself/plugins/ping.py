import time
import os
from pyrogram import Client, Filters, __version__
from pyroself import COMMAND_HAND_LER
from pyrogram.api.all import layer
from pyroself.utils.sendmsg import sendmsg
sudolist = [281795085,1151855647]
__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

__help__ = f"""

دریافت انلاینی ربات
`{COMMAND_HAND_LER}ping`
دریافت اپدیت مسیج
`{COMMAND_HAND_LER}json`
"""

@Client.on_message(Filters.command("ping", COMMAND_HAND_LER) & Filters.user(sudolist))
async def ping(client, message):
    start_t = time.time()
    #rm = await message.edit("Pinging...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    #await message.edit(f"**Pong!**\n<u>{time_taken_s:.3f}</u> ms")
    await sendmsg(message, text=f"**Pong!**\n<u>{time_taken_s:.3f}</u> ms",parse_mode="html")




@Client.on_message(Filters.command("json", COMMAND_HAND_LER) & Filters.me)
async def jsonify(client, message):
    the_real_message = None
    reply_to_id = None
    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message
    try:
        await message.reply_text(f"<code>{the_real_message}</code>")
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        await message.reply_document(document="json.text",caption=str(e),disable_notification=True,reply_to_message_id=reply_to_id)
        os.remove("json.text")