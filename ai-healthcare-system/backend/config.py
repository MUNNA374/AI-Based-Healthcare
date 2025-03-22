from pymongo import MongoClient

MONGO_URI = "mongodb+srv://sahasantanu38:19uvb41zqpQBsRlM@ai-healthcare-db.gvvwy.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client.healthcare
patients_collection = db.patients
