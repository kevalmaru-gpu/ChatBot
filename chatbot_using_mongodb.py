import custom_logic_adapter
from chatterbot import ChatBot
from chatterbot import trainers
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import filters

bot = ChatBot(
    'English Bot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapter=[
        {
            'import_path': 'custom_logic_adapter.MyLogicAdapter'
        }
    ],
)

print('Type something to begin...')

while True:
    try:
        user_input = input()
        
        bot_response = bot.get_response(user_input)

        print(bot_response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break