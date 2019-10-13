from tkinter import *

window = Tk()
window.title("Entry form")
window.geometry("300x500")

#code goes here...
topframe = Frame(window)
topframe.grid(column=0,row=0)

bottomframe = Frame(window)
bottomframe.grid(column=0,row=1)

namelabel = Label(topframe, text = "Name")
namelabel.pack(side = "left")

nameEntry = Entry(topframe, background = "white", justify = "center")
nameEntry.pack(side= "right")

phonelabel = Label(bottomframe, text = "Phone Number")
phonelabel.pack(side = "left")

phoneEntry = Entry(bottomframe, background = "white", justify = "center")
phoneEntry.pack(side= "right")

window.mainloop()
