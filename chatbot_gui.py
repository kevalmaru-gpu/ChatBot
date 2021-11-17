# db url
# mongodb+srv://admin992:8733981820@cluster0.mgtom.mongodb.net/prj1?retryWrites=true&w=majority

from tkinter import *

from pymongo import MongoClient

#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient("mongodb+srv://admin992:8733981820@cluster0.mgtom.mongodb.net/prj1?retryWrites=true&w=majority")
db = client.business



user_info = {
    "name": "",
    "number": "",
    "address": "",
    "a_name": "",
    "a_symptoms": "",
}

def send(info):    
    message = "You ->" + e.get()
    txt.insert(END, "\n" + message)

    # convert the input text to lower case for case issues
    input_text = str(e.get()).lower()

    if e.get() == 'hi' or e.get() == 'hello' or e.get() == 'my animal is not ok' or e.get() == 'i need help':
        txt.insert(END, "\n"+"Bot -> Please Enter your name.")
    elif input_text.startswith("my name is"):
        info["name"] = str(e.get()).split(" ",3)[3]
        txt.insert(END, "\n"+f"Bot -> Ok, please enter your number.")
    elif input_text.startswith("my number is"):
        info["number"] = str(e.get()).split(" ",3)[3]
        txt.insert(END, "\n"+f"Bot -> Ok, please enter your address.")
    elif input_text.startswith("my address is"):
        info["address"] = str(e.get()).split(" ",3)[3]
        txt.insert(END, "\n"+f"Bot -> Ok, what is your animal name?")
    elif input_text.startswith("my animal name is"):
        info["a_name"] = str(e.get()).split(" ",4)[4]
        txt.insert(END, "\n"+f"Bot -> Ok, what are the symptoms?")
    elif input_text.startswith("symptoms are,"):
        info["a_symptoms"] = str(e.get()).split(" ",2)[2]
        result=db.chatbot_user.insert_one(user_info)

        if info["name"] == "" or info["number"] == "" or info["address"] == "" or info["a_name"] == "" or info["a_symptoms"] == "":
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



