from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import sys

cwd = os.getcwd()

root3 = Tk()
root3.geometry("450x200")
root3.resizable(False, False)
root3.title("Discord Cloud Storage (Made By: The Low Spec PC)")
root3.iconbitmap(cwd + "/icon.ico")
root3.config(bg="gray")

Label(root3, text="Enter Folder Name", font=("Raleway", 15)).place(x=140, y=10)
Entry(root3, width="25").place(x=150, y=70)

#Label(root3, text="Folder Created", font=("Raleway", 10)).place(x=180, y=110)
#Label(root3, text="Folder Deleted", font=("Raleway", 10)).place(x=180, y=110)

Button(root3, text="Create", width="15", height="2").grid(row=0, column=0, padx=70, pady=150)
Button(root3, text="Delete", width="15", height="2").grid(row=0, column=1, padx=10, pady=150)

root3.mainloop()