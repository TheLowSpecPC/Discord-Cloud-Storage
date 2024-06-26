from secrets import Your_Token
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from functools import partial
from subprocess import call
import nextcord
from nextcord.ext import commands
import threading
import sys
import os

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

try:
    left_over = os.listdir(cwd + "\\out\\")
    if len(left_over) > 0:
        for i in left_over:
            fold = os.listdir(cwd + f"\\out\\{i}\\")
            if len(fold) > 0:
                for j in fold:
                    os.remove(cwd + f"\\out\\{i}\\" + j)
            os.rmdir(cwd + f"\\out\\{i}\\")
except:
    print(EXCEPTION)


print(file)
print(folder)

root = Tk()
root.geometry("560x600")
root.resizable(False,False)
root.title("Discord Cloud Storage (Made By: The Low Spec PC)")
root.iconbitmap(cwd+"/icon.ico")
root.config(bg="gray")

# main
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# scrollbar
my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set, bg="gray")
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas, width = 1000, height = 100, bg="gray")

def menu(files):
    def download():
        root1.destroy()
        if os.path.exists(cwd + f"\\out\\{files}\\"):
            fr = os.listdir(cwd + f"\\out\\{files}\\")

            for i in range(len(fr)):
                fr[i] = cwd + f"\\out\\{files}\\" + fr[i]
            for i in range(len(fr)):
                if os.path.exists(fr[i]):
                    os.remove(fr[i])
        else:
            os.mkdir(cwd + f"\\out\\{files}\\")

        call(["python", f"dbot.py", "download", files])

    def delete():
        root1.destroy()
        call(["python", f"dbot.py", "delete", files])

    root1 = Tk()
    root1.geometry("450x200")
    root1.resizable(False, False)
    root1.title(files)
    root1.iconbitmap(cwd + "/icon.ico")
    root1.config(bg="gray")

    Button(root1, text="Download", command=threading.Thread(target=download).start, width="15", height="2").grid(row=0, column=0, padx=70, pady=70)
    Button(root1, text="Delete", command=threading.Thread(target=delete).start, width="15", height="2").grid(row=0, column=1, padx=10, pady=70)

    root1.mainloop()

def upload(key):
    dir = filedialog.askopenfilename(initialdir="C:/", title="Select a Video")

    def thread():
        call(["python", f"dbot.py", "send", dir, key])

    th = threading.Thread(target=thread)
    th.start()

def folder_options(folders):
    def callcre(fold):
        root3.destroy()
        call(["python", f"dbot.py", "folder", fold, "cre"])
    def calldel(fold):
        root3.destroy()
        call(["python", f"dbot.py", "folder", fold, "del"])

    root3 = Tk()
    root3.geometry("450x200")
    root3.resizable(False, False)
    root3.title("Folder Options")
    root3.iconbitmap(cwd + "/icon.ico")
    root3.config(bg="gray")

    Label(root3, text="Enter Folder Name", font=("Raleway", 15)).place(x=140, y=10)
    fol = Entry(root3, width="25")
    fol.place(x=150, y=50)

    name = []
    for i in range(len(folders)):
        name.append(list(folders.keys())[i])

    def callback(input):
        if "." not in input and " " not in input and input != "null":
            return True
        else:
            return False

    def cre():
        if callback(fol.get()) == True and fol.get() != "":
            if fol.get() not in name:
                callcre(fol.get())

            else:
                Label(root3, text="Folder already exist", font=("Raleway", 10)).place(x=165, y=110)

        elif callback(fol.get()) == False or fol.get() == "":
            Label(root3, text="Invalid Character", font=("Raleway", 10)).place(x=175, y=110)

    def dele():
        if callback(fol.get()) == True and fol.get() != "":
            if fol.get() in name:
                calldel(fol.get())

            else:
                Label(root3, text="Folder does not exist", font=("Raleway", 10)).place(x=164, y=110)

        elif callback(fol.get()) == False or fol.get() == "":
            Label(root3, text="Invalid Character", font=("Raleway", 10)).place(x=175, y=110)

    Button(root3, text="Create", command=threading.Thread(target=cre).start, width="15", height="2").grid(row=0,
                                                                                                          column=0,
                                                                                                          padx=70,
                                                                                                          pady=150)
    Button(root3, text="Delete", command=threading.Thread(target=dele).start, width="15", height="2").grid(row=0,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=150)

    root3.mainloop()

def folder_menu(files, key):
    root4 = Tk()
    root4.geometry("560x600")
    root4.resizable(False, False)
    root4.title(key)
    root4.iconbitmap(cwd + "/icon.ico")
    root4.config(bg="gray")

    # main
    main_frame1 = Frame(root4)
    main_frame1.pack(fill=BOTH, expand=1)

    # canvas
    my_canvas1 = Canvas(main_frame1)
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # scrollbar
    my_scrollbar1 = tk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # configure the canvas
    my_canvas1.configure(yscrollcommand=my_scrollbar1.set, bg="gray")
    my_canvas1.bind('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    second_frame1 = Frame(my_canvas1, width=1000, height=100, bg="gray")

    Button(second_frame1, text="Upload", command= partial(upload, key), width="15", height="2").grid(row=0, column=0, padx=10, pady=8)

    a = 1
    i = 0
    f = True

    while i < len(files):
        if f == True:
            Button(second_frame1, text=files[i], command= partial(menu, files[i]), width="35", height="2").grid(row=a, column=0, padx=10, pady=8)
            f = False
            i += 1
        if i < len(files) and f == False:
            Button(second_frame1, text=files[i], command= partial(menu, files[i]), width="35", height="2").grid(row=a, column=1, padx=10, pady=8)
            f = True
            i += 1
        else:
            break
        a += 1

    my_canvas1.create_window((0, 0), window=second_frame, anchor="nw")
    root4.mainloop()

def exit():
    sys.exit(1)

root.wm_protocol("WM_DELETE_WINDOW", exit)

Button(second_frame, text="Upload", command= partial(upload, "null"), width="15", height="2").grid(row = 0, column = 0, padx = 10, pady = 8)
Button(second_frame, text="Folder Options", command= partial(folder_options, folder), width="15", height="2").grid(row=0, column=1, padx=10, pady=8)

a=1
i=0
f = True

while i < len(folder):
    if f == True:
        Button(second_frame, text=list(folder.keys())[i], command=partial(folder_menu, folder[list(folder.keys())[i]], list(folder.keys())[i]), width="35", height="2").grid(row = a, column = 0, padx = 10, pady = 8)
        f=False
        i+=1

    if i < len(folder) and f == False:
        Button(second_frame, text=list(folder.keys())[i], command=partial(folder_menu, folder[list(folder.keys())[i]], list(folder.keys())[i]), width="35", height="2").grid(row = a, column = 1, padx = 10, pady = 8)
        f=True
        i+=1

    else:
        break
    a+=1

i=0
while i < len(file):
    if f == True:
        Button(second_frame, text=file[i], command= partial(menu, file[i]), width="35", height="2").grid(row = a, column = 0, padx = 10, pady = 8)
        f=False
        i+=1
    if i < len(file) and f == False:
        Button(second_frame, text=file[i], command= partial(menu, file[i]), width="35", height="2").grid(row = a, column = 1, padx = 10, pady = 8)
        f=True
        i+=1
    else:
        break
    a+=1

my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
root.mainloop()