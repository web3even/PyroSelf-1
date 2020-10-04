from pyrogram import Message, Client
from inspect import getfullargspec

async def sendmsg(message: Message, **kwargs):
    func = message.edit if message.from_user.is_self else message.reply
    spec = getfullargspec(func).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})