# Laeeqah Esau Class 2

from tkinter import *
from datetime import datetime
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("Ithuba National Lottery of South Africa")
window.configure(background = "maroon")


lage = Label(window, text = "Your Age")
lage.pack(padx = 0, pady = 0)


lage_ent = Entry(window)
lage_ent.pack(padx = 1, pady = 2)

def login():
    import random

    if int(lage_ent.get()) >= 18:
        messagebox.showinfo("MESSAGE","You entered the Lottery")


        window = Tk()
        window.geometry("500x500")
        window.title("Lottery Game")
        window.configure(background = "maroon")


        heading = Label(window, text = "Winner")
        heading.pack()

        e1 = Entry(window, width = 5, bd = 5)
        e1.place(x = 100, y = 50)
        e2 = Entry(window,width = 5, bd = 5)
        e2.place(x = 150, y = 50)
        e3 = Entry(window, width = 5, bd = 5)
        e3.place(x = 200, y = 50)
        e4 = Entry(window, width = 5, bd = 5)
        e4.place(x = 250, y = 50)
        e5 = Entry(window, width = 5, bd = 5)
        e5.place(x = 300, y = 50)
        e6 = Entry(window, width = 5, bd = 5)
        e6.place(x = 350, y = 50)

    def roll():
        a = random.randint(1, 49)
        b = random.randint(1, 49)
        c = random.randint(1, 49)
        d = random.randint(1, 49)
        e = random.randint(1, 49)
        f = random.randint(1, 49)

        num1.set(a)
        num2.set(b)
        num3.set(c)
        num4.set(d)
        num5.set(e)
        num6.set(f)
        return


    num1 = StringVar()
    num2 = StringVar()
    num3 = StringVar()
    num4 = StringVar()
    num5 = StringVar()
    num6 = StringVar()



    btn2 = Button(window, text = "Draw", command = roll)
    btn2.pack(pady = 70)


btn = Button(window, text = "Login", command = login)
btn.pack()




window.mainloop()
