import time, requests, os, urllib
from pyrogram import Client, Filters, __version__
from pyroself import COMMAND_HAND_LER
from pyrogram.api.all import layer
from pyroself.utils.sendmsg import sendmsg
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

__help__ = f"""
راهنمای بخش فان

دریافت عکس کون
`{COMMAND_HAND_LER}kon`
دریافت عکس ممه
`{COMMAND_HAND_LER}mme`
"""

def drawtext(text, text_color, background_color):
    global tg_img
    font_size = 20
    font = ImageFont.truetype("pyroself/utils/font/CascadiaCodePL.ttf", font_size)
    width = font.getsize(max(text.split('\n'), key=len))[0] + 35
    height = font.getsize(text.split('\n')[0])[1] * text.count('\n') + 40
    img = Image.new('RGB', (width, height), color=f'{background_color}')
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), text, font=font, fill=f'{text_color}')

    tg_img = BytesIO()
    tg_img.name = 'tg.png'
    img.save(tg_img, 'PNG')
    tg_img.seek(0)
    return tg_img

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




@Client.on_message(Filters.command('tti', COMMAND_HAND_LER) & filters.me)
async def text_to_img(client, message):
    global tg_img
    text_color = message.command[1]
    background_color = message.command[2]
    text = ' '.join(message.command[3:])

    if text == '':
        if message.reply_to_message:
            await message.delete()
            text = message.reply_to_message.text
            drawtext(text, text_color, background_color)
            await client.send_photo(message.chat.id, tg_img, reply_to_message_id=message.reply_to_message.message_id)
    else:
        await message.delete()
        drawtext(text, text_color, background_color)
        if message.reply_to_message == None:
            await client.send_photo(message.chat.id, tg_img)
        else:
            await client.send_photo(message.chat.id, tg_img, reply_to_message_id=message.reply_to_message.message_id)