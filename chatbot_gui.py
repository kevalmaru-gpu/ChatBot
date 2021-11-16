from tkinter import *

root = Tk()
root.configure(background="black")

name = ""
number = ""
email = ""

def send():
    message = "You ->" + e.get()
    txt.insert(END, "\n" + message)

    if e.get() == 'hi' or e.get() == 'hello' or e.get() == 'my animal is not ok' or e.get() == 'i need help':
        txt.insert(END, "\n"+"Bot -> Please Enter your name.")
    elif str(e.get()).startswith("my name is"):
        name = str(e.get()).split(" ",3)[3]
        txt.insert(END, "\n"+f"Bot -> Ok, please enter your number.")
    elif str(e.get()).startswith("my number is"):
        number = str(e.get()).split(" ",3)[3]
        txt.insert(END, "\n"+f"Bot -> Ok, please enter your email.")
    elif str(e.get()).startswith("my email is"):
        email = str(e.get()).split(" ",3)[3]
        txt.insert(END, "\n"+f"Bot -> Ok, thank you.")
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
