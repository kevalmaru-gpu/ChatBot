from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("bot",storage_adapter='chatterbot.storage.MongoDatabaseAdapter')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

while True:
    query = str(input(">>"))
    response = bot.get_response(query)
    print(response)

    if "exit" in query:
        break
