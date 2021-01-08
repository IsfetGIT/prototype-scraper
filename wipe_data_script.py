from pymongo import MongoClient

client = MongoClient('mongodb+srv://isfet:Dinamik97@carabinieri.vcunl.mongodb.net/scraped_data?retryWrites=true&w=majority')

db = client.scraped_data
collection = db.scraped_data

collection.remove()
