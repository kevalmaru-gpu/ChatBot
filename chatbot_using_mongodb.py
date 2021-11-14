from chatterbot import ChatBot

bot = ChatBot(
    'bot',
    storage_adapter = 'chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'
)

while True:
    try:
        