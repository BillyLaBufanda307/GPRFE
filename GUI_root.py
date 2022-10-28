import tkinter as tk

#Establish base for GUI as variable root
root = tk.Tk()
root.geometry("1000x1000")
root.title("GPRFE")

#created basic heading named Datframe as variable heading 
heading = tk.Label(root, text="Dataframe",borderwidth=0.5, relief="ridge",  font=('Arial', 18))
heading.place(x=10, y=50, width = 200, height= 50)

#create basic query entry box where SQL scripts could extract data from??\
#qbH = tk.Label(root, text="QUERY",borderwidth=0.5, relief="raised",  font=('Arial', 10))
#qbH.pack(ipady=10, anchor=tk.NE)
querybox = tk.Entry(qbH, borderwidth=0.5, relief="sunken")#replace qbH???
querybox.pack()
#querybox.pack(ipady=10, anchor=tk.NE)

root.mainloop()