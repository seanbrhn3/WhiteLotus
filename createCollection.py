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
    t = task[1:]
    print(t)
    db.tasks.remove({"task" : t})
    return "{} has been completed".format(task)

def all_tasks_test(task):
    t = []
    print(task)
    for i in db.tasks.find():
        if i == i['task']:
            print("YAH WE GOT IT")
        else:
            print(i['task'])
            print("BITCH IDK WHATS GOING ON")


#print(all_tasks())
