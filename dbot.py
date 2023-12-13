import nextcord, os, shutil
from nextcord.ext import commands
import sys, re
from secrets import Your_Token

token = Your_Token
intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)
cwd = os.getcwd()


def send(dir):
    @bot.event
    async def on_ready():
        flag_tmp = dir.split("\\")[len(dir.split("\\")) - 1]
        flag = flag_tmp.split("/")[len(flag_tmp.split("/")) - 1]
        file = os.listdir(cwd + "\\out")
        channel = bot.get_channel(1116747276275155024)
        channel_flag = bot.get_channel(1180390532703326210)

        for i in range(len(file)):
            file[i] = cwd + "\\out\\" + file[i]

        print(f'{bot.user} has connected to Discord!')

        async for message in channel_flag.history(limit=None):
            con = message.content
            check = con.split(" ", 1)
            if re.sub("\(.*?\)", "()", check[1]) == re.sub("\(.*?\)", "()", "()"+flag):
                substrings = []
                in_brackets = False
                current_substring = ""

                for c in check[1]:
                    if c == "(":
                        in_brackets = True
                    elif c == ")" and in_brackets:
                        substrings.append(current_substring)
                        current_substring = ""
                        in_brackets = False
                    elif in_brackets:
                        current_substring += c

                if current_substring:
                    substrings.append(current_substring)

                flag = f'({int(substrings[0])+1})'+flag
                break

            elif check[1] == flag:
                flag = '(1)' + flag

        await channel_flag.send(content=str(len(file)) + ' ' + flag)

        for i in range(len(file)):
            await channel.send(file=nextcord.File(file[i]), content= flag+str(i+1))
            print(file[i])
            if os.path.exists(file[i]):
                os.remove(file[i])

        await bot.close()

    bot.run(token)

def down(file):
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
        channel = bot.get_channel(1116747276275155024)
        channel_flag = bot.get_channel(1180390532703326210)
        folder = os.listdir(cwd + "\\out")
        contents = []
        names = []
        for i in range(len(folder)):
            folder[i] = cwd + "\\out\\" + folder[i]
        for i in range(len(folder)):
            if os.path.exists(folder[i]):
                os.remove(folder[i])

        async for message in channel_flag.history(limit=None):
            con = message.content
            flag = con.split(" ", 1)
            if flag[1] == file:
                totalpart = int(flag[0])
                for i in range(totalpart):
                    names.append(file + str(i + 1))
                print(names)
                break

        a=0
        async for message in channel.history(limit=None):
            content = message.content
            contents.append(content)

            if a <= len(names):
                if content in names:
                    for attachment in message.attachments:
                        print(attachment.filename)
                        await attachment.save(attachment.filename)
                        shutil.move(cwd+"\\"+attachment.filename,
                                        cwd +"\\out\\"+attachment.filename)
                        a+=1
            else:
                break

        await bot.close()

    bot.run(token)

def dele(file):
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
        channel = bot.get_channel(1116747276275155024)
        channel_flag = bot.get_channel(1180390532703326210)
        folder = os.listdir(cwd + "\\out")
        contents = []
        names = []
        for i in range(len(folder)):
            folder[i] = cwd + "\\out\\" + folder[i]
        for i in range(len(folder)):
            if os.path.exists(folder[i]):
                os.remove(folder[i])

        async for message in channel_flag.history(limit=None):
            con = message.content
            flag = con.split(" ", 1)
            if flag[1] == file:
                totalpart = int(flag[0])
                for i in range(totalpart):
                    names.append(file + str(i + 1))
                print(names)
                break

        a=0
        async for message in channel.history(limit=None):
            content = message.content
            contents.append(content)

            if a <= len(names):
                if content in names:
                    await message.delete()
                    a+=1
            else:
                break

        async for message in channel_flag.history(limit=None):
            con = message.content
            flag = con.split(" ", 1)
            if flag[1] == file:
                await message.delete()
                break

        await bot.close()

    bot.run(token)

if sys.argv[1] == "send":
    send(sys.argv[2])
elif sys.argv[1] == "download":
    down(sys.argv[2])
elif sys.argv[1] == "delete":
    dele(sys.argv[2])