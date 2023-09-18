import os

from pymongo.mongo_client import MongoClient

# client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6")
client = MongoClient(os.environ.get('MONGODB_URI'))
# print(os.environ.get('MONGODB_URI'))
db = client.pokemon_db

collection_name = db["pokemon_collection"]