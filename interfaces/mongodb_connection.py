
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["interface_info"]
collection = db["interface_data"]
