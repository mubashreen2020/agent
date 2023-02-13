import pymongo

def connect_mongodb():
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Return the client
    return client
