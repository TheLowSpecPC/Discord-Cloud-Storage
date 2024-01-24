from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import sys

cwd = os.getcwd()

a={}

for i in range(10):
    a["Somthing"+str(i)]=[]
for j in range(10):
    for k in range(j):
        a["Somthing"+str(j)].append(k)
#print(len(a))
#print(a[list(a.keys())[8]])

con1 = "28 null test.png"
flag1 = con1.split(" ", 2)
print(flag1[2])