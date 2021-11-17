from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin992:8733981820@cluster0.mgtom.mongodb.net/prj1?retryWrites=true&w=majority")
db = client.business


fivestar = db.chatbot_user.find_one({'name': "chintan"})
print(fivestar)
