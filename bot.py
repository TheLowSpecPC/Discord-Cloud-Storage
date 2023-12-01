import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)


def send(file):
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
        channel = bot.get_channel(1116747276275155024)
        for i in range(len(file)):
            await channel.send(file=discord.File(file[i]))
        await bot.close()

    bot.run('Your Token')