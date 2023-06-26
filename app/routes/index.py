from flask import Blueprint, render_template, redirect, request, url_for, jsonify
from app.db import db
from datetime import datetime
from bson.objectid import ObjectId
from pymongo import ReturnDocument
from app.models.task import Task

task_router = Blueprint("task_router", __name__)


@task_router.route("/")
def index():
    tasks = db.tasks.find()
    task_list = list(tasks)
    return render_template("index.html", task_list=task_list)


@task_router.route("/new-task", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("create.html")
    elif request.method == "POST":
        user = request.form.get("user")
        startingPoint = request.form.get("startingPoint")
        endPoint = request.form.get("endPoint")
        amount = float(request.form.get("amount"))
        reason = request.form.get("reason")
        date = request.form.get("date")
        new_task = Task(
            user,
            startingPoint,
            endPoint,
            amount,
            reason,
            date,
            datetime.now(),
            None,
            None,
        )

        db.tasks.insert_one(new_task.to_json())

    return redirect(url_for("task_router.index")), 201


@task_router.route("/task", defaults={"id": None})
@task_router.route("/task/", defaults={"id": None})
@task_router.route("/task/<id>")
def task(id=None):
    # Si no me envias un ID, te regreso al index:
    if id == None:
        return redirect("/")
    # Si me envias un ID entonces trato de extraer la tarea con ese ID:
    task = db.tasks.find_one(ObjectId(id))

    if task == None:
        return redirect("/")
    # Si la tarea no está vacía Entonces se la mando al template:
    return render_template("detail.html", task=task)


@task_router.route("/done", methods=["POST"])
def done():
    task_id = request.form.get("id")
    next = request.form.get("next")
    task = db.tasks.find_one_and_update(
        {"_id": ObjectId(task_id)},
        {"$set": {"doneAt": datetime.now()}},
        upsert=False,
        return_document=ReturnDocument.AFTER,
    )
    if task == None:
        return redirect("/")
    if next != None:
        return redirect(next)
    return redirect("/task/" + str(task_id))


@task_router.route("/delete/<id>", methods=["POST"])
def delete(id):
    if request.method == "POST":
        task = db.tasks.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": {"deletedAt": datetime.now()}},
            upsert=False,
            return_document=ReturnDocument.AFTER,
        )
        if task is None:
            return redirect("/")
        return redirect("/task/" + str(id))


@task_router.route("/update-task/<id>", methods=["GET", "PUT"])
def update_task(id):
    task = db.tasks.find_one({"_id": ObjectId(id)})

    if request.method == "GET":
        return render_template("update.html", task=task)
    elif request.method == "PUT":
        new_user = request.form.get("user")
        new_starting_point = request.form.get("startingPoint")
        new_end_point = request.form.get("endPoint")
        new_amount = request.form.get("amount")
        new_reason = request.form.get("reason")
        new_date = request.form.get("date")
        task = db.tasks.find_one_and_update(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "user": new_user,
                    "startingPoint": new_starting_point,
                    "endPoint": new_end_point,
                    "amount": new_amount,
                    "reason": new_reason,
                    "date": new_date,
                }
            },
            upsert=False,
            return_document=ReturnDocument.AFTER,
        )
    return jsonify({"message": "Job updated successfully"}), 200
