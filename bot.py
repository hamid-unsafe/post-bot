from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import events
from telethon import functions, types
import telethon
from bot_functions import *
import requests
# import urllib.request

# trust = requests.get('https://hamid814.github.io/public-js/trust.json').json()['trust']

# print(trust)

client_name = 'poster-client'
bot_name = 'poster-bot'
API_ID = 1759413
API_HASH = '609e3756b5a95466c9422ab57eea37bb'
BOT_TOKEN = '1345211056:AAFR3DP5XNfHtQWosz2xZkqV9kkpcSJK9fc'

chatId = None
destChatId = None

# r = urllib.request.urlopen('https://hamid814.github.io/public-js/trust.json')
# print(r.read())

client = TelegramClient(client_name, API_ID, API_HASH)
bot = TelegramClient(bot_name, API_ID, API_HASH)

client.start()
bot.start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage)
async def bot_new_message_handler(event):
  if(event.raw_text.startswith('/')):
    command = event.raw_text.split('/')[1]
    
    await botCommandRecieved(event, command)

@client.on(events.NewMessage)
async def new_message_handler(event):
  global chatId
  global destChatId
  
  # check if its not telegram official account
  if event.message.from_id != 777000:
    # check if its recieving message
    if event.out == False:
      message = await client(functions.channels.GetMessagesRequest(
        channel=event.message.to_id.channel_id,
        id=[event.message.id]
      ))

      await client.send_message('@autopostingnewbot', message.messages[0])

async def joinChannel(id):
  channel = await client.get_entity(id)
  
  await client(JoinChannelRequest(channel))

async def botCommandRecieved(event, command):
  global chatId
  global destChatId
  
  if command == 'start':
    chat = await event.get_chat()

    chatId = chat.id

    await event.respond('you will get new messages here')

  # set destination channel
  elif command.startswith('setdest'):
    channelId = command.split(' ')[1]

    destChatId = channelId

    await event.respond('channel saved')
    
  # add channel command
  elif command.startswith('addchannel'):
    channelId = command.split(' ')[1]

    isIdValid = await validateChannelId(channelId, bot)

    if isIdValid:
      try:
        await joinChannel(channelId)

        await event.respond('channel added')
      except:
        await event.respond('there was a problem')

    else:
      await event.respond('id is not a valid channel')

  else:
    await event.respond('default command response: ' + command)

client.run_until_disconnected()
