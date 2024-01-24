import nextcord, os
from nextcord.ext import commands
from secrets import Your_Token

token = Your_Token
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    channel_flag = bot.get_channel(1116747276275155024)
    async for message in channel_flag.history(limit=None):
        await message.delete()

    await bot.close()
bot.run(token)