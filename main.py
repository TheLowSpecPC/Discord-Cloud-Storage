import FileConverter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sys
import threading
import nextcord, os, shutil
from nextcord.ext import commands
from subprocess import call

token = 'Your Token'
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

    pb = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='indeterminate',
        length=280
    )
    pb.place(x=120, y=180)
    pb.start()
    value_label = ttk.Label(root, text=f"Wait till the process is done")
    value_label.place(x=185, y=210)

    FileConverter.split(dir)
    call(["python", f"dbot.py", "send", dir])

    value_label['text'] = "File successfully uploaded"
    pb.stop()

def download():
    file = don.get()

    pb = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='indeterminate',
        length=280
    )
    pb.place(x=120, y=180)
    pb.start()
    value_label = ttk.Label(root, text=f"Wait till the process is done")
    value_label.place(x=185, y=210)

    call(["python", f"dbot.py", "download", file])
    FileConverter.join(file)

    value_label['text'] = "File successfully downloaded"
    pb.stop()

def delete():
    file = de.get()

    pb = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='indeterminate',
        length=280
    )
    pb.place(x=120, y=180)
    pb.start()
    value_label = ttk.Label(root, text=f"Wait till the process is done")
    value_label.place(x=185, y=210)

    call(["python", f"dbot.py", "delete", file])

    value_label['text'] = "File successfully deleted"
    pb.stop()

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
Button(root,text="Delete", command=threading.Thread(target=delete).start, width="10", height="1").place(x=300, y=150)

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