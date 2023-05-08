from flask import Blueprint, render_template, redirect, request
from app.db import db
from datetime import datetime
from bson.objectid import ObjectId
from bson import json_util
import json
from pymongo import ReturnDocument

task_router = Blueprint("task_router", __name__)

#
# Inicio de las rutas del app (sección tareas):
#
@task_router.route("/")
def index():
    tasks = db.tasks.find()
    task_list = list(tasks)
    return render_template("index.html", lista_tareas=task_list)

@task_router.route("/add", methods=["POST"])
def add():
    task_text = request.form.get("text") # Recupero lo que viene en el input del form
    if task_text == "" or task_text == None:
        return redirect("/")
    
    newTask = {
        "text": task_text,
        "createdAt": datetime.now(),
        "doneAt": None,
        "deletedAt": None,
    }
    db.tasks.insert_one(newTask)

    return redirect("/")


@task_router.route("/update/<id>", methods=["PUT"])
def update(id):
    text = request.form.get("text")
    task = db.tasks.find_one_and_update({'_id':ObjectId(id)}, {"$set": {"text": text}}, upsert=False, return_document=ReturnDocument.AFTER)
    return parse_json(task), 200

def parse_json(data):
    return json.loads(json_util.dumps(data))


@task_router.route("/task", defaults={'id': None})
@task_router.route("/task/", defaults={'id': None})
@task_router.route("/task/<id>")

def task(id = None):
    # Si no me envias un ID, te regreso al index:
    if id == None:
        return redirect("/")
    # Si me envias un ID entonces trato de extraer la tarea con ese ID:
    task = db.tasks.find_one(ObjectId(id))
    print(task['text'])
    if task == None:
        return redirect("/")
    # Si la tarea no está vacía Entonces se la mando al template:
    return render_template("detail.html", task=task)

@task_router.route("/done", methods=["POST"])
def done():
    task_id = request.form.get("id")
    next = request.form.get("next")
    task = db.tasks.find_one_and_update({'_id':ObjectId(task_id)}, {"$set": {"doneAt": datetime.now()}}, upsert=False, return_document=ReturnDocument.AFTER)
    if task == None:
        return redirect("/")
    if next != None:
        return redirect(next)
    return redirect("/task/" + str(task_id))

@task_router.route("/delete/<id>")
def delete(id):
    task = db.tasks.find_one_and_update({'_id':ObjectId(id)}, {"$set": {"deletedAt": datetime.now()}}, upsert=False, return_document=ReturnDocument.AFTER)
    if task == None:
        return redirect("/")
    
    return redirect("/task/" + str(id))