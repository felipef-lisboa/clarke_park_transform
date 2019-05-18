#! /usr/bin/python3

# Tkinter test
print('Tkinter tests\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Clark's and Park's Transformations")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

phaseA = StringVar()
phaseB = StringVar()
phaseC = StringVar()

ttk.Label(mainframe, text="Phase A:").grid(column=1, row=1, sticky=W)
phaseA_entry = ttk.Entry(mainframe, width=7, textvariable=phaseA)
phaseA_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Phase B:").grid(column=1, row=2, sticky=W)
phaseB_entry = ttk.Entry(mainframe, width=7, textvariable=phaseB)
phaseB_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Phase C:").grid(column=1, row=3, sticky=W)
phaseC_entry = ttk.Entry(mainframe, width=7, textvariable=phaseC)
phaseC_entry.grid(column=2, row=3, sticky=(W, E))


root.mainloop()