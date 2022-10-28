from tkinter import *
from tkinter import filedialog

#Establish base for GUI as variable root
root = Tk()
root.geometry("1000x500")
root.title("GPRFE")

#created basic heading named Datframe as variable heading 
heading = Label(root, text="Dataframe",borderwidth=0.5, relief="ridge",  font=('Arial', 10))
heading.pack(side='top', anchor='nw')

#Open file explorer script
def openfile():
    filename= filedialog.askopenfilenames(initialdir="/", title="Select Files", filetypes= ())
    #create location to indicate opened file
    fileindicatorframe=LabelFrame(root, padx=10, pady=10) #create frame to keep things organized
    fileindicatorframe.pack(side='top', anchor='se') #set location of frame WIP
    fileindicator= Label(root, borderwidth= 5, relief="sunken", width=100, text=filename) #create fileindicator label as variabel "fileindicator"
    fileindicator.pack() #pack label into fileindicatorframe
    return

#create basic button to import file
importframe = LabelFrame(root, padx=10, pady=10) #create frame to keep things organized
importframe.pack(side='top', anchor='ne', padx=10)#set location of frame
fileimport = Button(importframe, text= "Import", padx=10, pady=10, command=openfile) 
#create button for importing files as variable "fileimport"
#command=openfile calls open file script
fileimport.pack() #pack button into importframe


root.mainloop()