import pymongo

client = pymongo.MongoClient("mongodb://localhost:27018")
db = client.get_database("prediction_service")

data_collection = db.get_collection("data")

data = list(data_collection.find())

data

data[45]

len(data)