from flask import Flask, render_template, request, redirect, url_for
from  taskTracker import TaskTracker
from pymongo import MongoClient
import datetime
import urllib.parse
import createCollection
app = Flask(__name__)
tracker = TaskTracker()


client = MongoClient("mongodb+srv://root:" + urllib.parse.quote("Ab45305006@")+"@cluster0-8mszk.mongodb.net/test?retryWrites=true")
db = client.test


@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        print(request.form)
        if 'delete' in request.form:
            print("reached?")
            createCollection.delete_all()
        elif  "complete" in request.form:
            fun = request.form["complete"].split("Complete:")
            the_task = fun[1]
            createCollection.completed_task(the_task)
            return redirect(url_for("completed",task=the_task))
        elif "submit" in request.form:
            db.tasks.insert_one({
                "task": request.form['task'],
                "date": datetime.datetime.now(),
                "completed": False
            })
        return redirect(url_for("index"))
    return render_template("index.html",tasks=db.tasks.find())

@app.route("/completed/<task>", methods=["GET","POST"])
def completed(task):
    createCollection.completed_task(task)
    return render_template("completed.html",task=task)

if __name__ == "__main__":
    app.run(debug=True)
