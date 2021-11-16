from tkinter import *

root = Tk()
root.configure(background="black")


def send():
    message = "You ->" + e.get()
    txt.insert(END, "\n" + message)

    if e.get() == 'hi' or e.get() == 'hello' or e.get() == 'my animal is not ok' or e.get() == 'i need help':
        txt.insert(END, "\n"+"Bot -> Please Enter your name.")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry I didn't get you")

    e.delete(0, END)



txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
send_button = Button(root, text="send", command=send).grid(row=1, column=1)

e.grid(row=1, column=0)
root.title("ChatBot")

root.mainloop()
