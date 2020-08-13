import os
from pyrogram import Client, Filters
from pyroself import MAX_MESSAGE_LENGTH, COMMAND_HAND_LER
from pyroself.plugins import ALL_PLUGINS
from pyroself import HELP_COMMANDS

HELP_DEFAULT = f"""
برای دریافت راهنمای سلف ابتدا دستور
`plugins`
لیست پلاگین های سلف ارسال میشود برای دریافت راهنمای هر پلاگین بصورت زیر عمل کنید...
`help` نام پلاگین
"""

@Client.on_message(Filters.command("plugins", COMMAND_HAND_LER) & Filters.me)
async def list_plugins(client, message):
    mods = ""
    mod_num = 0
    plugins = list(HELP_COMMANDS.keys())
    for plug in plugins:
        mods += f"`{plug}`\n"
        mod_num += 1
    all_plugins = f"<b>لیست پلاگین ها : <u>{mod_num}</u></b>\n\n" + mods
    await message.edit(all_plugins)
    return


@Client.on_message(Filters.command("help", COMMAND_HAND_LER) & Filters.me)
async def help_me(client, message):
    if len(message.command) == 1:
        await message.edit(HELP_DEFAULT)
    elif len(message.command) == 2:
        module_name = message.text.split(" ",1)[1]
        try:
            HELP = f"**راهنمای پلاگین {module_name}**\n" + HELP_COMMANDS[f'{module_name}']
            await message.reply_text(HELP, parse_mode="md", disable_web_page_preview=True)
            await message.delete()
        except Exception as ef:
            await message.edit(f"<b>خطا:</b>\n\n{ef}")
    else:
        await message.edit(f"دستور وارد شده اشتباه است")
    return