import gprpy.gprpy as gp
import os
import tkinter as tk
from tkinter import filedialog as fd
mygpr = gp.gprpyProfile()
filelist = []
truncx = []
truncy = []
os.chdir("/Users/katrinacristino/Desktop/gprfiles")


def pickx():
    global truncx
    xlist1 = ''
    xlist2 = ''
    xlist1 == x_position_entry1.get()
    xlist2 == x_position_entry2.get()
    int(xlist1)
    int(xlist2)
    truncx.append(xlist1)
    truncx.append(xlist2)
    return truncx


def picky():
    global truncy
    ylist1 = ''
    ylist2 = ''
    ylist1 == y_position_entry1.get()
    ylist2 == y_position_entry2.get()
    int(ylist1)
    int(ylist2)
    truncy.append(ylist1)
    truncy.append(ylist2)
    return truncy


def iterate(path):
    for file in os.listdir(path):
        if file.endswith(".DT1"):
            filelist.append(path + file)
    #filesbox = tk.Label(root, relief="sunken", text=filelist)
    #filesbox.grid(column=0, row=6, columnspan=2, rowspan=3)
    return filelist


def openfile():
    global folder_path
    foldername = fd.askdirectory(initialdir="/", title="Select folder")
    # define entry
    fileindicator = tk.Label(root, borderwidth=5, relief="sunken", width=100, text=foldername)
    fileindicator.grid(column=0, row=5, columnspan=2, rowspan=1)
    folder_path = foldername
    if folder_path == foldername:
        iterate(folder_path)
    return folder_path


def exportfile(x, y):
    for file in filelist:
        filename = file[:-3] + "pdf"
        mygpr.importdata(file)
        mygpr.printProfile(filename, color='gray', contrast=10, yrng=y, xrng=x, dpi=600)


# defining the root
root = tk.Tk()
folder_path = ""
root.title("Automatic Processing")
root.geometry("500x1000")
root.resizable(width=False, height=True)

# define buttons
import_file = tk.Button(root, text="Import", font="Arial", relief="raised", padx=10, pady=10, command=openfile)
export_file = tk.Button(root, text="Export", font="Arial", relief="raised", padx=10, pady=10, command=lambda: exportfile(truncx, truncy))

set_time = tk.Button(root, text="Set 0 Time", font="Arial", relief="raised", padx=10, pady=10)
set_time_entry = tk.Entry(root, relief="sunken")

x_position = tk.Button(root, text="Truncate x", font="Arial", relief="raised", padx=10, pady=10, command=pickx)
x_position_entry1 = tk.Entry(root, relief="sunken")
x_position_entry2 = tk.Entry(root, relief="sunken")

y_position = tk.Button(root, text="Truncate y", font="Arial", relief="raised", padx=10, pady=10, command=picky)
y_position_entry1 = tk.Entry(root, relief="sunken")
y_position_entry2 = tk.Entry(root, relief="sunken")

wow = tk.Button(root, text="Dewow", font="Arial", relief="raised", padx=10, pady=10)

# place buttons
import_file.grid(column=1, row=0, columnspan=1, rowspan=1)
export_file.grid(column=0, row=0, columnspan=1, rowspan=1)

set_time.grid(column=0, row=1, columnspan=1, rowspan=1)
set_time_entry.grid(column=1, row=1, columnspan=1, rowspan=1)

x_position.grid(column=0, row=2, columnspan=1, rowspan=1)
x_position_entry1.grid(column=1, row=2, columnspan=1, rowspan=1)
x_position_entry2.grid(column=2, row=2, columnspan=1, rowspan=1)

y_position.grid(column=0, row=3, columnspan=1, rowspan=1)
y_position_entry1.grid(column=1, row=3, columnspan=1, rowspan=1)
y_position_entry2.grid(column=2, row=3, columnspan=1, rowspan=1)

wow.grid(column=0, row=4, columnspan=2, rowspan=1)


root.mainloop()


