from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("savan",storage_adapter='chatterbot.storage.MongoDatabaseAdapter')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

def input_query():
    query = str(input(">>"))
    response = bot.get_response(query)
    return response

while True:
    query = str(input(">>"))
    response = bot.get_response(query)
    print(response)

    if response == "What is your name ?":
        resp = input_query()
        print(resp)
        if resp == "What is your number ?":
            resp = input_query()
            print(resp)
            if resp == "What is your address ?":
                resp = input_query()
                print(resp)
                if resp == "Ok we will register you":
                    print("Registered successfully")
                else:
                    print("Try again")
            else:
                print("Try again")
        else:
            print("Try again")
    else:
        print("Try again")


    if "exit" in query:
        break
