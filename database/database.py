from pymongo.mongo_client import MongoClient

# Create a new client and connect to the server
client = MongoClient("mongodb+srv://ignatylimansky:root@cluster0.muigmmg.mongodb.net/?retryWrites=true&w=majority")

db = client.pokemon_db
# Send a ping to confirm a successful connection

collection_name = db["pokemon_collection"]


# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
