# db url
# mongodb+srv://admin992:8733981820@cluster0.mgtom.mongodb.net/prj1?retryWrites=true&w=majority

from tkinter import *
from pymongo import MongoClient, results

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

grammer_words = ["my","is","a","an","are","not","like","name","number","address","animal","symptoms","symtoms","symtom","symptom",","," "]

def find_word(to_find,array):
    """
        this function will return any particular word from list of string
    """
    for i in array:
        if i == to_find:
            return True

    return False

def differ_entity(array):
    """
        this function will return any word or list of word which are not grammer_word list and could be user data
    """
    is_differ = None
    entities = []

    for i in array: # looping through string list
        for y in grammer_words: # looping a string list through grammer_word list
            """
            if once the string element is equal to one of the grammer_word list element
            then is_differ will set to false which is sign that it is not a user data
            is_differ will stay True if the string is user data
            """
            if i == y:
                is_differ = False 
        
        # appending string
        if is_differ == True:
            entities.append(i)
        
        is_differ = True

    if len(entities) == 1: # if user has provided data in one word
        return entities[0]
    elif len(entities) == 0: # if user havent provided any data
        return 0
    elif len(entities) > 1: # if user has provided multiple data (Which will return a list)
        return entities 


def send(info):    
    message = "You ->" + e.get()
    txt.insert(END, "\n" + message)

    # convert the input text to lower case for case issues
    input_text = str(e.get()).lower()
    # spliting input sentence into array
    input_text_array = input_text.split(" ")

    if e.get() == 'hi' or e.get() == 'hello' or e.get() == 'my animal is not ok' or e.get() == 'i need help':
        txt.insert(END, "\n"+"Bot -> Please Enter your name.")
    elif find_word("name",input_text_array) and find_word("animal",input_text_array) == False:
        # getting user info
        differed_entity = differ_entity(input_text_array)

        if differed_entity != 0 and type(differed_entity) != list: # checking if it isnt a list
            # directly add to dict
            info["name"] = differed_entity 

            txt.insert(END, "\n"+f"Bot -> Ok, please enter your number.")
            print(differed_entity)
        elif differed_entity != 0 and type(differed_entity) == list: # if it is a list
            final_sentence = ""
            # adding all words of list with space in between
            for i in differed_entity:
                final_sentence = final_sentence + " " + i
            info["name"] = final_sentence.lstrip()
            txt.insert(END, "\n"+f"Bot -> Ok, please enter your number.")
            print(info["name"])
        else:
            txt.insert(END, "\n"+f"Bot -> Invalid response.")

    elif find_word("number",input_text_array):
        differed_entity = differ_entity(input_text_array)

        if differed_entity != 0:
            info["number"] = differed_entity
            txt.insert(END, "\n"+f"Bot -> Ok, please enter your address.")
            print(differed_entity)
        else:
            txt.insert(END, "\n"+f"Bot -> Invalid response.")

    elif find_word("address",input_text_array):
        differed_entity = differ_entity(input_text_array)

        if differed_entity != 0 and type(differed_entity) != list:
            info["address"] = differed_entity
            txt.insert(END, "\n"+f"Bot -> Ok, what is your animal name?")
            print(differed_entity)
        elif differed_entity != 0 and type(differed_entity) == list:
            final_sentence = ""
            for i in differed_entity:
                final_sentence = final_sentence + " " + i
            info["address"] = final_sentence.lstrip()
            txt.insert(END, "\n"+f"Bot -> Ok, what is your animal name?")
            print(final_sentence)
        else:
            txt.insert(END, "\n"+f"Bot -> Invalid response.")

    elif ((find_word("animal",input_text_array) and find_word("name",input_text_array))):
        differed_entity = differ_entity(input_text_array)

        if differed_entity != 0:
            info["a_name"] = differed_entity
            txt.insert(END, "\n"+f"Bot -> Ok, what is your animal symptoms?")
            print(differed_entity)
        else:
            txt.insert(END, "\n"+f"Bot -> Invalid response.")
            
    elif find_word("symptoms",input_text_array) or find_word("symptoms",input_text_array) or find_word("symtom",input_text_array):
        #result=db.chatbot_user.insert_one(user_info)

        differed_entity = differ_entity(input_text_array)

        if differed_entity != 0 and type(differed_entity) != list:
            info["a_symptoms"] = differed_entity
            print(differed_entity)
        elif differed_entity != 0 and type(differed_entity) == list:
            final_sentence = ""
            for i in differed_entity:
                final_sentence = final_sentence + " " + i
            info["a_symptoms"] = final_sentence.lstrip()
            print(final_sentence)
        else:
            txt.insert(END, "\n"+f"Bot -> Invalid response.")
            return

        if info["name"] == "" or info["number"] == "" or info["address"] == "" or info["a_name"] == "" or info["a_symptoms"] == "":
            txt.insert(END, "\n"+f"Bot -> Please provide your,")
            if info["name"] == "":
                txt.insert(END, "\n\t"+f"Name")
            if info["number"] == "":
                txt.insert(END, "\n\t"+f"Number")
            if info["address"] == "":
                txt.insert(END, "\n\t"+f"Address")
            if info["a_name"] == "":
                txt.insert(END, "\n\t"+f"Animal name")
            if info["a_symptoms"] == "":
                txt.insert(END, "\n\t"+f"Symptoms of your animal")
        else:
            # conversation will end here
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

<<<<<<< HEAD
root.mainloop()
=======
root.mainloop()
>>>>>>> 97291e0ab336883791da52e084cf13790b119bfc
