import nextcord, os, shutil
from nextcord.ext import commands
import sys, re
import threading
from time import sleep
from tkinter import *
from tkinter import ttk
from secrets import Your_Token

token = Your_Token
intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)
cwd = os.getcwd()

def send(dir, folder):
    root1 = Tk()
    root1.geometry("450x200")
    root1.resizable(False, False)
    root1.title("Upload")
    root1.iconbitmap(cwd + "/icon.ico")
    root1.config(bg="gray")

    pb = ttk.Progressbar(
        root1,
        orient=HORIZONTAL,
        mode="determinate",
        length=280
    )
    pb.place(x=85, y=70)
    value_label = ttk.Label(root1, text=f"Current Progress: 0.00%")
    value_label.place(x=160, y=120)

    def update_progress_label():
        return f"Current Progress: {pb['value']:.2f}%"

    def thread():
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

            pb['value'] = 5
            value_label['text'] = update_progress_label()

            async for message in channel_flag.history(limit=None):
                con = message.content
                check = con.split(" ", 2)
                if re.sub("\(.*?\)", "()", check[2]) == re.sub("\(.*?\)", "()", "()"+flag):
                    substrings = []
                    in_brackets = False
                    current_substring = ""

                    for c in check[2]:
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

                elif check[2] == flag:
                    flag = '(1)' + flag
                    break

            await channel_flag.send(content=str(len(file)) + ' ' + folder + ' ' + flag)

            for i in range(len(file)):
                sleep(1)
                await channel.send(file=nextcord.File(file[i]), content= flag+str(i+1))
                print(file[i])
                if os.path.exists(file[i]):
                    os.remove(file[i])

                pb['value'] += 95/len(file)
                value_label['text'] = update_progress_label()
                if i+1 == len(file):
                    pb['value'] = 100
                    value_label['text'] = update_progress_label()

            await bot.close()

        bot.run(token)

    th = threading.Thread(target=thread)
    th.start()

    root1.mainloop()

def down(file):
    root2 = Tk()
    root2.geometry("450x200")
    root2.resizable(False, False)
    root2.title("Download")
    root2.iconbitmap(cwd + "/icon.ico")
    root2.config(bg="gray")

    pb = ttk.Progressbar(
        root2,
        orient=HORIZONTAL,
        mode="determinate",
        length=280
    )
    pb.place(x=85, y=70)
    value_label = ttk.Label(root2, text=f"Current Progress: 0.00%")
    value_label.place(x=160, y=120)

    def update_progress_label():
        return f"Current Progress: {pb['value']:.2f}%"

    def thread():
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
                flag = con.split(" ", 2)
                if flag[2] == file:
                    totalpart = int(flag[0])
                    for i in range(totalpart):
                        names.append(file + str(i + 1))
                    print(names)
                    break

            pb['value'] = 5
            value_label['text'] = update_progress_label()

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

                            pb['value'] += 95 / len(names)
                            value_label['text'] = update_progress_label()
                            if a == len(names):
                                pb['value'] = 100
                                value_label['text'] = update_progress_label()
                            a+=1
                else:
                    break

            await bot.close()

        bot.run(token)

    th = threading.Thread(target=thread)
    th.start()

    root2.mainloop()

def dele(file):
    root3 = Tk()
    root3.geometry("450x200")
    root3.resizable(False, False)
    root3.title("Delete")
    root3.iconbitmap(cwd + "/icon.ico")
    root3.config(bg="gray")

    pb = ttk.Progressbar(
        root3,
        orient=HORIZONTAL,
        mode="determinate",
        length=280
    )
    pb.place(x=85, y=70)
    value_label = ttk.Label(root3, text=f"Current Progress: 0.00%")
    value_label.place(x=160, y=120)

    def update_progress_label():
        return f"Current Progress: {pb['value']:.2f}%"

    def thread():
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
                flag = con.split(" ", 2)
                if flag[2] == file:
                    totalpart = int(flag[0])
                    for i in range(totalpart):
                        names.append(file + str(i + 1))
                    print(names)
                    break

            pb['value'] = 10
            value_label['text'] = update_progress_label()

            a=0
            async for message in channel.history(limit=None):
                content = message.content
                contents.append(content)

                if a <= len(names):
                    if content in names:
                        await message.delete()

                        pb['value'] += 85 / len(names)
                        value_label['text'] = update_progress_label()
                        a+=1
                else:
                    break

            async for message in channel_flag.history(limit=None):
                con = message.content
                flag = con.split(" ", 2)
                if flag[2] == file:
                    await message.delete()
                    pb['value'] = 100
                    value_label['text'] = update_progress_label()
                    break

            await bot.close()

        bot.run(token)

    th = threading.Thread(target=thread)
    th.start()

    root3.mainloop()

def credel_folder(folder, check):
    root4 = Tk()
    root4.geometry("450x200")
    root4.resizable(False, False)
    if check == "cre":
        root4.title("Create Folder")
    elif check == "del":
        root4.title("Delete Folder")
    root4.iconbitmap(cwd + "/icon.ico")
    root4.config(bg="gray")

    pb = ttk.Progressbar(
        root4,
        orient=HORIZONTAL,
        mode="determinate",
        length=280
    )
    pb.place(x=85, y=70)
    value_label = ttk.Label(root4, text=f"Current Progress: 0.00%")
    value_label.place(x=160, y=120)

    def update_progress_label():
        return f"Current Progress: {pb['value']:.2f}%"

    def thread():
        @bot.event
        async def on_ready():
            print(f'{bot.user} has connected to Discord!')
            channel = bot.get_channel(1116747276275155024)
            channel_flag = bot.get_channel(1180390532703326210)
            folder_flag = bot.get_channel(1199825547077898392)
            names = []
            contents = []
            files = []

            if check == "cre":
                async for message in folder_flag.history(limit=None):
                    content = message.content
                    names.append(content)
                    pb['value'] = 50
                    value_label['text'] = update_progress_label()

                if folder not in names:
                    await folder_flag.send(content=folder)
                    pb['value'] = 100
                    value_label['text'] = update_progress_label()

            elif check == "del":
                names = []
                async for message in channel_flag.history(limit=None):
                    con = message.content
                    flag = con.split(" ", 2)
                    if flag[1] == folder:
                        files.append(flag[2])

                pb['value'] = 5
                value_label['text'] = update_progress_label()

                if len(files) > 0:
                    f = 85/len(files)
                else:
                    f = 85

                for file in files:
                    async for message in channel_flag.history(limit=None):
                        con = message.content
                        flag = con.split(" ", 2)
                        if flag[2] == file:
                            totalpart = int(flag[0])
                            for i in range(totalpart):
                                names.append(file + str(i + 1))
                            break
                        print(names)

                    pb['value'] = 5
                    value_label['text'] = update_progress_label()

                    a = 0
                    async for message in channel.history(limit=None):
                        content = message.content
                        contents.append(content)

                        if a <= len(names):
                            if content in names:
                                await message.delete()
                                pb['value'] += f/len(names)
                                value_label['text'] = update_progress_label()
                                a += 1
                        else:
                            break

                    async for message in channel_flag.history(limit=None):
                        con = message.content
                        flag = con.split(" ", 2)
                        if flag[2] == file:
                            await message.delete()
                            break

                async for message in folder_flag.history(limit=None):
                    content = message.content
                    if content == folder:
                        await message.delete()
                        pb['value'] = 100
                        value_label['text'] = update_progress_label()
                        break

            await bot.close()
        bot.run(token)

    th = threading.Thread(target=thread)
    th.start()

    root4.mainloop()

if sys.argv[1] == "send":
    send(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "download":
    down(sys.argv[2])
elif sys.argv[1] == "delete":
    dele(sys.argv[2])
elif sys.argv[1] == "folder":
    credel_folder(sys.argv[2], sys.argv[3])