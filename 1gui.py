""" importing the necessary modules for a gui"""

from tkinter import *
import sys
from tkinter.ttk import*
root = Tk()
root.title("RATE THIS BOOTCAMP?") #text that appers on title bar
selected = IntVar()
rad1 = Radiobutton(root,text='ONE', value=1, variable=selected)#build radio buttons
rad2 = Radiobutton(root,text='TWO', value=2, variable=selected)
rad3 = Radiobutton(root,text='THREE', value=3, variable=selected)
def clicked():
   print(selected.get()) #print the user input
btn = Button(root, text="Click Me", command=clicked)
rad1.grid(column=0, row=0) #pistion of the radio buttons
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
root.mainloop()            #continue to loop until the program is closed


sys.exit(0)                #exit and return status
