from tkinter import *
import random
import sys

window = Tk()
window.geometry("500x500")
window.title("Ithuba National Lottery of South Africa")
window.configure(background = "maroon")


lage = Label(window, text = "Your Age")
lage.pack(padx = 0, pady = 0)

lage_ent = Entry(window)
lage_ent.pack(padx = 1, pady = 2)

def choose():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

random = Label(window, text = "Winner")
random.pack()

btn = Button(window, text = "Press", command = choose)




window.mainloop()
