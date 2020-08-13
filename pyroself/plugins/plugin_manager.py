from os import execl, path, remove
from sys import executable
from pyrogram import Client, Filters
from pyroself import COMMAND_HAND_LER
from pyroself.plugins import ALL_PLUGINS
from pyroself.utils.pyrohelpers import ReplyCheck

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

__help__ = f"""

برای ارسال پلاگین
`{COMMAND_HAND_LER}sendpl` نام پلاگین
نصب پلاگین
`{COMMAND_HAND_LER}installpl` ریپلای روی پلاگین
حذف کردن پلاگین
`{COMMAND_HAND_LER}delpl` نام پلاگین
ریلود کردن سلف
`{COMMAND_HAND_LER}reload`
"""

@Client.on_message(Filters.command("reload", COMMAND_HAND_LER) & Filters.me)
async def reloads(client, message):
    await message.edit("`ربات با موفقیت بروز شد!!`")
    execl(executable, executable, "-m", "pyroself")

@Client.on_message(Filters.command("sendpl", COMMAND_HAND_LER) & Filters.me)
async def send_plugin(client, message):
    if len(message.text.split(" ")) == 1:
        await message.edit("`دستور وارد شده اشتباه است!!`")
        return
    await message.edit("`در حال ارسال پلاگین...`")
    plugin_name = message.text.split(" ",1)[1]
    if plugin_name not in ALL_PLUGINS:
        await message.edit(f"نام پلاگین وارد شده اشتباه است!\nبا ارسال دستور `{COMMAND_HAND_LER}plugins`. لیست پلاگین های خود را ببینید!")
        return
    await message.reply_document(
                document=f"/app/pyroself/plugins/{plugin_name}.py",
                caption=f"**پلاگین :** `{plugin_name}.py`",
                disable_notification=True,
                reply_to_message_id=ReplyCheck(message))
    await message.delete()
    return


@Client.on_message(Filters.command("installpl", COMMAND_HAND_LER) & Filters.me)
async def install_plugin(client, message):
    if len(message.command) == 1 and message.reply_to_message.document:
        if message.reply_to_message.document.file_name.split(".")[-1] != "py":
            await message.edit("`فقط میتوانید فایل های پایتون نصب کنید!!!`")
            return
        plugin_loc = f"/app/pyroself/plugins/{message.reply_to_message.document.file_name}"
        await message.edit("`در حال نصب پلاگین...`")
        if os.path.exists(plugin_loc):
            await message.edit(f"`پلاگین {message.reply_to_message.document.file_name} از قبل نصب شده بود!!`")
            return
        try:
            plugin_dl_loc = await client.download_media(
                message=message.reply_to_message,
                file_name=plugin_loc)
            if plugin_dl_loc:
                await message.edit(f"**پلاگین مورد نظر نصب شد :** {message.reply_to_message.document.file_name}")
        except Exception as e_f:
            await message.edit(f"**خطا:**\n`{e_f}`")
    return


@Client.on_message(Filters.command("delpl", COMMAND_HAND_LER) & Filters.me)
async def delete_plugin(client, message):
    if len(message.command) == 2:
        plugin_loc = f"/app/pyroself/plugins/{message.command[1]}.py"
        if os.path.exists(plugin_loc):
            os.remove(plugin_loc)
            await message.edit(f"**پلاگین مورد نظر حذف شد:** {message.command[1]}")
            return
        await message.edit("`چنین پلاگینی وجود ندارد!!`")
        return
    await message.edit("`دستور وارد شده اشتباه است!!`")
    return
