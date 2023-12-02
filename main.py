import FileConverter
from tkinter import *
from tkinter import filedialog
import sys
import threading
import nextcord, os, shutil
from nextcord.ext import commands

token = 'Your TOKEN'
intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)
cwd = os.getcwd()

root = Tk()
root.geometry("520x600")
root.title("Discord Cloud Storage (Made By: The Low Spec PC)")
root.iconbitmap(cwd+"/icon.ico")
root.config(bg="gray")

def upload():
    dir = filedialog.askopenfilename(initialdir="C:/", title="Select a Video")

    FileConverter.split(dir)
    @bot.event
    async def on_ready():
        flag = dir.split("\\")[len(dir.split("\\")) - 1]
        file = os.listdir(cwd + "\\out")
        name = file[0].split(".", 1)[0]
        for i in range(len(file)):
            file[i] = cwd + "\\out\\" + file[i]

        print(f'{bot.user} has connected to Discord!')
        channel = bot.get_channel(1116747276275155024)
        for i in range(len(file)):
            await channel.send(file=nextcord.File(file[i]), content=name + str(i + 1))
            if os.path.exists(file[i]):
                os.remove(file[i])

        channel_flag = bot.get_channel(1180390532703326210)
        await channel_flag.send(content=str(len(file)) + ' ' + flag)
        async for message in channel_flag.history():
            con = message.content
            flag = con.split(" ", 1)
            cmd.delete('1.0', END)
            cmd.insert(END, flag[1] + "\n")

        await bot.close()

    bot.run(token)

def download():
    file = don.get()

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
                    shutil.move(cwd + "\\" + attachment.filename,
                                cwd + "\\out\\" + attachment.filename)

        await bot.close()

    bot.run(token)

    FileConverter.join(file)

def delete():
    file = de.get()

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
                await message.delete()

        async for message in channel_flag.history():
            con = message.content
            flag = con.split(" ", 1)
            cmd.delete('1.0', END)
            cmd.insert(END, flag[1] + "\n")

        async for message in channel.history():
            content = message.content
            contents.append(content)

            if content in names:
                await message.delete()

        await bot.close()

    bot.run(token)

def exit():
    sys.exit(1)

def temp_text3(e):
    don.delete(0,"end")
def temp_text4(e):
    de.delete(0,"end")

Label(root, text="File Upload", font=("Raleway", 20), bg="black", fg="white", height="1").place(x=175, y=1)

Label(root, text="File Name", font=("Raleway", 20), bg="black", fg="white", height="1").place(x=185, y=70)
don = Entry(root, width="20")
don.insert(0, "Eg: temp.mp4")
don.place(x=170, y=120)
don.bind("<FocusIn>", temp_text3)

de = Entry(root, width="20")
de.insert(0, "Eg: temp.mp4")
de.place(x=170, y=150)
de.bind("<FocusIn>", temp_text4)

Button(root,text="Download", command=threading.Thread(target=download).start, width="10", height="1").place(x=300, y=120)
Button(root,text="Delete", command=delete, width="10", height="1").place(x=300, y=150)

Button(root, text="Upload", command=threading.Thread(target=upload).start, width="20", height="2").place(x=185, y=250)

root.wm_protocol("WM_DELETE_WINDOW", exit)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
cmd = Text(root, width="60", height="17")
cmd.place(x=10, y=300)
scrollbar.config(command=cmd.yview)
cmd.config(yscrollcommand=scrollbar.set)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    channel_flag = bot.get_channel(1180390532703326210)
    async for message in channel_flag.history():
        con = message.content
        flag = con.split(" ", 1)
        cmd.insert(END, flag[1]+"\n")
    await bot.close()
bot.run(token)

root.mainloop()