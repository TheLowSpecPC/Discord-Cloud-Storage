import nextcord, os, shutil
from nextcord.ext import commands

token = 'Your TOKEN'
intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)
cwd = os.getcwd()


def send(dir):
    @bot.event
    async def on_ready():
        flag = dir.split("\\")[len(dir.split("\\"))-1]
        file = os.listdir(cwd + "\\out")
        name = file[0].split(".",1)[0]
        for i in range(len(file)):
            file[i] = cwd + "\\out\\" + file[i]

        print(f'{bot.user} has connected to Discord!')
        channel = bot.get_channel(1116747276275155024)
        for i in range(len(file)):
            await channel.send(file=nextcord.File(file[i]), content= name+str(i+1))
            if os.path.exists(file[i]):
                os.remove(file[i])

        channel_flag = bot.get_channel(1180390532703326210)
        await channel_flag.send(content=str(len(file))+' '+flag)

        await bot.close()

    bot.run(token)

def down(file):
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
        channel = bot.get_channel(1116747276275155024)
        channel_flag = bot.get_channel(1180390532703326210)
        folder = os.listdir(cwd + "\\out")
        name = file.split(".")[0]
        contents = []
        names = []
        for i in range(len(folder)):
            folder[i] = cwd + "\\out\\" + folder[i]
        for i in range(len(folder)):
            if os.path.exists(folder[i]):
                os.remove(folder[i])

        async for message in channel_flag.history():
            con = message.content
            flag = con.split(" ", 1)
            if flag[1] == file:
                totalpart = int(flag[0])
                for i in range(totalpart):
                    names.append(name + str(i + 1))
                print(names)

        async for message in channel.history():
            content = message.content
            contents.append(content)

            if content in names:
                for attachment in message.attachments:
                    print(attachment.filename)
                    await attachment.save(attachment.filename)
                    shutil.move(cwd+"\\"+attachment.filename,
                                    cwd +"\\out\\"+attachment.filename)

        await bot.close()

    bot.run(token)