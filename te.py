from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import threading
from subprocess import call
import os
import sys

cwd = os.getcwd()

root3 = Tk()
root3.geometry("450x200")
root3.resizable(False, False)
root3.title("Folder Options")
root3.iconbitmap(cwd + "/icon.ico")
root3.config(bg="gray")

Label(root3, text="Enter Folder Name", font=("Raleway", 15)).place(x=140, y=10)
fol = Entry(root3, width="25")
fol.place(x=150, y=50)

def cre():
    pb = ttk.Progressbar(
        root3,
        orient='horizontal',
        mode='indeterminate',
        length=280
    )
    pb.place(x=85, y=80)
    pb.start()

#    call(["python", f"dbot.py", "folder", fol.get(), "cre"])

    pb.stop()
    Label(root3, text="Folder Created", font=("Raleway", 10)).place(x=180, y=110)

def dele():
    pb = ttk.Progressbar(
        root3,
        orient='horizontal',
        mode='indeterminate',
        length=280
    )
    pb.place(x=85, y=80)
    pb.start()

#    call(["python", f"dbot.py", "folder", fol.get(), "del"])

    pb.stop()
    Label(root3, text="Folder Deleted", font=("Raleway", 10)).place(x=180, y=110)

Button(root3, text="Create", command=threading.Thread(target=cre).start, width="15", height="2").grid(row=0, column=0, padx=70, pady=150)
Button(root3, text="Delete", command=threading.Thread(target=dele).start, width="15", height="2").grid(row=0, column=1, padx=10, pady=150)

root3.mainloop()