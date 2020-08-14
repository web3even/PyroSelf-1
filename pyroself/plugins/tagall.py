
import os
from pyrogram import Client, Filters
from pyroself import COMMAND_HAND_LER
from pyroself.utils.parser import mention_html, mention_markdown

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

__help__ = f"""

دریافت لیست ممبران گروه جهت چت
`{COMMAND_HAND_LER}tagall`
"""

@Client.on_message(Filters.command(["tagall", "all"], COMMAND_HAND_LER) & Filters.me)
async def everyone(client, message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = "کصکشا بالا باشین \n\n"
    kek = client.iter_chat_members(message.chat.id)
    async for a in kek:
        if not a.user.is_bot:
            text += f"{mention_markdown(a.user.first_name,a.user.id)} -"
    if message.reply_to_message:
        await client.send_message(message.chat.id, text, reply_to_message_id=message.reply_to_message.message_id)
    else:
        await client.send_message(message.chat.id, text)

