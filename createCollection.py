from pymongo import MongoClient
import urllib.parse
client = MongoClient("mongodb+srv://root:"+urllib.parse.quote("Ab45305006@")+"@cluster0-8mszk.mongodb.net/test?retryWrites=true")

db = client.test

def create(collection):
    db.create_collection(collection)
    return "collection: {} created".format(collection)

def delete_all():
    db.tasks.remove()
    return "all values detroyed"

def completed_task(task):
    db.tasks.remove(db.tasks.find_one({'task':task}))
