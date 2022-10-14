from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017/nicepages")
db=cluster["nicepages"]
collection=db["nicepages"]
data = {"id": 1 , "uname": "akash", "email":"akash@gmail.com","password":"1234@1234" }
collection.insert_one(data)
print(collection)