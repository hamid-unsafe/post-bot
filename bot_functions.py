from telethon.tl.types import Channel

async def validateChannelId(id, bot):
  try:
    channel = await bot.get_entity(id)

    if type(channel) == Channel:
      return True
    else:
      return False

  except:
    return False