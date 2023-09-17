from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6")
# client = MongoClient("mongodb://db:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6")
db = client.pokemon_db

collection_name = db["pokemon_collection"]