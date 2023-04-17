from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://webmailhostwebdesignbytom:y@r@H49C572sgUV@cluster0.7hmh93h.mongodb.net/?retryWrites=true&w=majority")

db = cluster["test"]

collection = db["test"]

# post
post = {"_id": 0, "name": "tom", "scores": 5}

collection.insert_one(post)

