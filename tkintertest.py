from tkinter import *
from tkinter import ttk
from randomtest import word

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="VoterID --> " + word).grid(column=0, row=0)
# ttk.Button(frm, text="Update", command=root.destroy).grid(column=1, row=0)
# ttk.Button(frm, text="quit", command=root.destroy).grid(column=2, row=0)
root.mainloop()