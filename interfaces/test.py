import pymongo

# set up the MongoDB client and database
client = pymongo.MongoClient("mongodb+srv://mj:mj:Mujff%40r@reachmanage.fsjfoer.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# select the collection to insert into
collection = db.my_collection

# create the record to insert
record = {"name": "Mujffar Sayyad", "email": "mj@example.com"}

# insert the record into the collection
result = collection.insert_one(record)

# print the unique identifier (_id) of the inserted record
print(result.inserted_id)
