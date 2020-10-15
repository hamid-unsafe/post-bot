from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import asyncio

bot_name = 'test-bot'
API_ID = 1524689
API_HASH = '14d226885030df209468c3fe12979672'
BOT_TOKEN = '1345211056:AAGYfHCW8GRliU1hF3zWrGVHOH16PbwKiOg'

bot = TelegramClient(bot_name, API_ID, API_HASH)

bot.start(bot_token=BOT_TOKEN)

bot.send_message('@qqqqwwweeeerrr2', 'hey')
bot.send_message('@qqqqwwweeeerrr2', 'hoy')
bot.send_message('@qqqqwwweeeerrr2', 'hay')
