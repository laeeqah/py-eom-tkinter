# Laeeqah Esau Class 2

from tkinter import *
from datetime import *
from tkinter import messagebox



# The layout and function for the first window
window = Tk()
window.geometry("500x400")
window.title("Ithuba National Lottery of South Africa")
window.configure(background = "green")

# Label and Entry for age
header = Label(window, text = "Ithuba National Lottery" +"\n" + "of South Africa", font=("Sans-Serif",20 ,"bold", "underline"), bg = "green", fg = "white")
header.place(x = 100, y = 0)

lage = Label(window, text = "Your Age", bg = "green", fg = "white", font = 15)
lage.pack(padx = 0, pady = 100)

#date&time
now = datetime.now()
add_date = now.strftime("%d %B %Y")
today_date = now.strftime("%H: %M %p")
datetime = add_date+"\n"+today_date
lbd = Label(window, text = "", bg = "green", fg = "white")
lbd['text'] = datetime
lbd.place(x = 180, y = 300)

lage_ent = Entry(window)
lage_ent.place(x = 170, y = 150)


def login():
    message = ""
    #try/except
    try:
        # If not older than 18 will not enter.
        if int(lage_ent.get()) >= 18:
            messagebox.showinfo("MESSAGE","You entered the Lottery")
            message = "You entered the Lottery"
            run = window_2()
        else:
            messagebox.showwarning("Age warning","You are too young")
            message = "You are too young"
            lage_ent.delete(0, 'end')
    except ValueError:
        messagebox.showerror("Value Error", "Only Numbers are Allowed")
        message = "Only Numbers are Allowed"
    return True

def window_2():
    import random

    # Layout and function for the second window
    window = Tk()
    window.geometry("500x400")
    window.title("Lottery Game")
    window.configure(background = "green")


    # header for the second window
    heading = Label(window, text = "Winner", bg = "green", fg = "white" ,font = 15)
    heading.pack()

    # all the entries to put your numbers in
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

    label = Label(window, bg = "green" , fg = "white")
    label.place(x = 80, y = 150)

    lot_label = Label(window, bg = "green", fg = "white")
    lot_label.place(x =100, y = 200)

    #random non-repeating number generator
    while True:
        #random generator
        a = random.randint(1, 49)
        b = random.randint(1, 49)
        c = random.randint(1, 49)
        d = random.randint(1, 49)
        e = random.randint(1, 49)
        f = random.randint(1, 49)

        lotto_num = sorted([a, b, c, d, e, f]) # random number will display in 6 numbers
        lotto_num = list(dict.fromkeys(lotto_num))
        if len(lotto_num) < 6:
            continue
        else:
            print(lotto_num)
            break



    def roll():
        print("clicked")

        new_list = []
        for i in lotto_num:         #prints out the the label in tkinter
            temp = " " +str(i) + " "
            new_list.append(temp)

        label['text'] = "Winner Numbers are: "+str(new_list)
        try:
            lot1 = int(e1.get()) # user entry in tkinter
            lot2 = int(e2.get())
            lot3 = int(e3.get())
            lot4 = int(e4.get())
            lot5 = int(e5.get())
            lot6 = int(e6.get())
        except ValueError:
            messagebox.showerror("Value Error", "Need to be between 1 and 49 and cannot be Letters")

        user_entry = [lot1, lot2, lot3, lot4, lot5, lot6] # user entry

        counter = 0
        for i in range (6):     # counts the entry number in the tkinter
            print(user_entry[i])
            if user_entry[i] in lotto_num:
                counter += 1

        if counter == 0 or counter == 1:
            lot_label['text'] = 'Message: You had ' +str(counter)+ ' number(s) correct. \nYou won nothing'
        elif counter == 2:
            lot_label['text'] = 'Congratulations: You had ' +str(counter)+ ' numbers correct \nYou won 20.00'
        elif counter == 3:
            lot_label['text'] = 'Congratulations: You had ' +str(counter)+ ' numbers correct \nYou won 100.50'
        elif counter == 4:
            lot_label['text'] = 'Congratulations: You had ' +str(counter)+ ' numbers correct \nYou won 2,384.00'
        elif counter == 5:
            lot_label['text'] = 'Congratulations: You had ' +str(counter)+ ' numbers correct \nYou won 8,584.00'
        elif counter == 6:
            lot_label['text'] = 'Congratulations: You had ' +str(counter)+ ' number(s) correct \nYou won 10,000000.00'

        with open("lottery_results.txt", "w+") as results:  # will show the lottery numbers, how much you won and the current date in the textfile
            for i in range(1):
                results_f = lot_label.cget("text") + "\n" + label.cget("text") + "\n" + lbd.cget("text")
                results.write(results_f)

    # button for the def roll()
    btn2 = Button(window, text = "Draw", command = roll, bg = "blue", fg = "white")
    btn2.pack(pady = 70)

# button for the def login()
btn = Button(window, text = "Login", command = login, bg = "blue", fg = "white")
btn.place(x = 220, y = 200)


window.mainloop()
