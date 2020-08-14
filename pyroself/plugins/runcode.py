import io
import os
import sys
import traceback
import time
import asyncio
import requests
from pyrogram import Client, Filters
from pyroself.utils.cust_p_filters import sudo_filter
from pyroself import MAX_MESSAGE_LENGTH, COMMAND_HAND_LER

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

__help__ = f"""

اجرای کد خود در ربات
`{COMMAND_HAND_LER}py کد`
"""


@Client.on_message(Filters.command(["eval", "py"], COMMAND_HAND_LER) & sudo_filter)
async def eval(client, message):
    status_message = await message.reply_text("`لطفا صبر کنید...`")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id

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
        evaluation = "بدونه مشکل"

    final_output = "<b>کد شما</b>: <code>{}</code>\n\n<b>نتیجه</b>:\n<code>{}</code> \n".format(
        cmd,
        evaluation.strip()
    )

    if len(final_output) > MAX_MESSAGE_LENGTH:
        with open("eval.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document="eval.text",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id
        )
        os.remove("eval.text")
        await status_message.delete()
    else:
        await status_message.edit(final_output)


async def aexec(code, client, message):
    exec(
        f'async def __aexec(client, message): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](client, message)

