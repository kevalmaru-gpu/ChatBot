from tkinter import *
from functools import partial

"""
    all user info will get stored in user_info dict
    
    in user_info dictionary 1 is name
                            2 is number
                            3 is address
                            4 is animal name
                            5 is animal symptoms
"""

user_info = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
}

def send(info):    
    message = "You ->" + e.get()
    txt.insert(END, "\n" + message)

    # convert the input text to lower case for case issues
    input_text = str(e.get()).lower()

    if e.get() == 'hi' or e.get() == 'hello' or e.get() == 'my animal is not ok' or e.get() == 'i need help':
        txt.insert(END, "\n"+"Bot -> Please Enter your name.")
    elif input_text.startswith("my name is"):
        info[1] = str(e.get()).split(" ",3)[3]
        txt.insert(END, "\n"+f"Bot -> Ok, please enter your number.")
    elif input_text.startswith("my number is"):
        info[2] = str(e.get()).split(" ",3)[3]
        txt.insert(END, "\n"+f"Bot -> Ok, please enter your address.")
    elif input_text.startswith("my address is"):
        info[3] = str(e.get()).split(" ",3)[3]
        txt.insert(END, "\n"+f"Bot -> Ok, what is your animal name?")
    elif input_text.startswith("my animal name is"):
        info[4] = str(e.get()).split(" ",4)[4]
        txt.insert(END, "\n"+f"Bot -> Ok, what are the symptoms?")
    elif input_text.startswith("symptoms are,"):
        info[5] = str(e.get()).split(" ",2)[2]

        if info[1] == "" or info[2] == "" or info[3] == "" or info[4] == "" or info[5] == "":
            txt.insert(END, "\n"+f"Bot -> You have not given us some of your information.")
        else:
            txt.insert(END, "\n"+f"Bot -> Ok, this is your solution.")
            print(info)
    else:
        txt.insert(END, "\n" + "Bot -> Sorry I didn't get you")

    e.delete(0, END)


root = Tk()
root.configure(background="black")

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
send_button = Button(root, text="send", command=lambda:send(user_info)).grid(row=1, column=1)

e.grid(row=1, column=0)
root.title("ChatBot")

root.mainloop()
