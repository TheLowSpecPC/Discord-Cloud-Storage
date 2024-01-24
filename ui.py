import FileConverter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sys
import threading
import nextcord, os
from nextcord.ext import commands
from subprocess import call
from secrets import Your_Token

cwd = os.getcwd()

token = Your_Token
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

folder = {}
file = []

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    channel_flag = bot.get_channel(1180390532703326210)
    folder_flag = bot.get_channel(1199825547077898392)

    async for message in folder_flag.history(limit=None):
        con1 = message.content
        folder[con1]=[]

    async for message in channel_flag.history(limit=None):
        con2 = message.content
        flag2 = con2.split(" ", 2)
        if flag2[1] == "null":
            file.append(flag2[2])
        else:
            folder[flag2[1]].append(flag2[2])

    await bot.close()
bot.run(token)

root = Tk()
root.geometry("550x600")
root.resizable(False,False)
root.title("Discord Cloud Storage (Made By: The Low Spec PC)")
root.iconbitmap(cwd+"/icon.ico")
root.config(bg="gray")

def menu():
    root1 = Tk()
    root1.geometry("450x200")
    root1.resizable(False, False)
    root1.title("Discord Cloud Storage (Made By: The Low Spec PC)")
    root1.iconbitmap(cwd + "/icon.ico")
    root1.config(bg="gray")

    def download():
        pb = ttk.Progressbar(
            root1,
            orient='horizontal',
            mode='indeterminate',
            length=280
        )
        pb.place(x=85, y=80)
        pb.start()
        value_label = ttk.Label(root1, text=f"Wait till the process is done")
        value_label.place(x=145, y=120)

        value_label['text'] = "File successfully downloaded"
        pb.stop()

    def delete():
        pb = ttk.Progressbar(
            root1,
            orient='horizontal',
            mode='indeterminate',
            length=280
        )
        pb.place(x=85, y=80)
        pb.start()
        value_label = ttk.Label(root1, text=f"Wait till the process is done")
        value_label.place(x=145, y=120)

        value_label['text'] = "File successfully deleted"
        pb.stop()

    Button(root1, text="Download", command=download, width="15", height="2").grid(row=0, column=0, padx=70, pady=15)
    Button(root1, text="Delete", command=delete, width="15", height="2").grid(row=0, column=1, padx=10, pady=15)

def upload():
    root2 = Tk()
    root2.geometry("450x200")
    root2.resizable(False,False)
    root2.title("Discord Cloud Storage (Made By: The Low Spec PC)")
    root2.iconbitmap(cwd + "/icon.ico")
    root2.config(bg="gray")

    pb = ttk.Progressbar(
        root2,
        orient='horizontal',
        mode='indeterminate',
        length=280
    )
    pb.place(x=85, y=70)
    pb.start()
    value_label = ttk.Label(root2, text=f"Wait till the process is done")
    value_label.place(x=160, y=120)

    value_label['text'] = "File successfully deleted"
    pb.stop()

def folder_options():
    root3 = Tk()
    root3.geometry("450x200")
    root3.resizable(False, False)
    root3.title("Discord Cloud Storage (Made By: The Low Spec PC)")
    root3.iconbitmap(cwd + "/icon.ico")
    root3.config(bg="gray")

    Label(root3, text="Enter Folder Name", font=("Raleway", 15)).place(x=140, y=10)
    Entry(root3, width="25").place(x=150, y=70)

    Button(root3, text="Create", width="15", height="2").grid(row=0, column=0, padx=70, pady=120)
    Button(root3, text="Delete", width="15", height="2").grid(row=0, column=1, padx=10, pady=120)

def folder_menu(files):
    root4 = Tk()
    root4.geometry("550x600")
    root4.resizable(False, False)
    root4.title("Discord Cloud Storage (Made By: The Low Spec PC)")
    root4.iconbitmap(cwd + "/icon.ico")
    root4.config(bg="gray")

    Button(root4, text="Upload", command=upload, width="15", height="2").grid(row=0, column=0, padx=10, pady=8)

    a = 1
    i = 0
    f = True
    while i < len(files):
        if f == True:
            Button(root, text=files[i], command=menu, width="35", height="2").grid(row=a, column=0, padx=10, pady=8)
            f = False
            i += 1
        if i < len(files) and f == False:
            Button(root, text=files[i], command=menu, width="35", height="2").grid(row=a, column=1, padx=10, pady=8)
            f = True
            i += 1
        else:
            break
        a += 1

def exit():
    sys.exit(1)

Button(root, text="Upload", command=upload, width="15", height="2").grid(row = 0, column = 0, padx = 10, pady = 8)
Button(root, text="Folder Options", command=folder_options, width="15", height="2").grid(row=0, column=1, padx=10, pady=8)

root.wm_protocol("WM_DELETE_WINDOW", exit)

"""for i in range(5):
    folder.append("folder "+str(i+1))
for i in range(9):
    file.append("file "+str(i+1))"""

a=1
i=0
f = True

while i < len(folder):
    if f == True:
        Button(root, text=list(folder.keys())[i], command=lambda: folder_menu(folder[list(folder.keys())[i]]), width="35", height="2").grid(row = a, column = 0, padx = 10, pady = 8)
        f=False
        i+=1

    if i < len(folder) and f == False:
        Button(root, text=list(folder.keys())[i], command=lambda: folder_menu(folder[list(folder.keys())[i]]), width="35", height="2").grid(row = a, column = 1, padx = 10, pady = 8)
        f=True
        i+=1

    else:
        break
    a+=1

i=0
while i < len(file):
    if f == True:
        Button(root, text=file[i], command=menu, width="35", height="2").grid(row = a, column = 0, padx = 10, pady = 8)
        f=False
        i+=1
    if i < len(file) and f == False:
        Button(root, text=file[i], command=menu, width="35", height="2").grid(row = a, column = 1, padx = 10, pady = 8)
        f=True
        i+=1
    else:
        break
    a+=1

root.mainloop()