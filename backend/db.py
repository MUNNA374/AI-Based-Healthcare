from pymongo import MongoClient

MONGO_URI = "mongodb+srv://sahasantanu38:sahasantanu38@ai-healthcare-db.gvvwy.mongodb.net/"
client = MongoClient(MONGO_URI)

db = client["ai_helthcare"]
collection = db["predictions"]

def save_prediction(data):
    collection.insert_one(date)
    print("data save by MONGODB. ")

