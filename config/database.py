from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/data_management")

db = client.data_management

sure_name_collection = db["sure_name"]
health_workers_collection = db["health_workers"]