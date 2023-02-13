from flask import Flask, request, jsonify
from db import models
from db.database import engine, SessionLocal
from db.models import TasksDB

# Initializing a database session
session = SessionLocal()

# Initializing a Flask application
app = Flask(__name__)


# Root path to test server
@app.route("/")
def index():
    return {"Message": "Server Running Successfully"}


# Route to get details about particular task
@app.route("/get/<int:task_id>", methods=["GET"])
def get_task(task_id):
    if request.method == "GET":
        try:
            task = session.query(TasksDB).filter(TasksDB.id == task_id).first()
            if task is None:
                return {"message": f"Task with id: {task_id} does not exist"}
            else:
                data = {
                    "id": task.id,
                    "name": task.name,
                    "is_completed": task.is_completed,
                }
                return data
        except:
            return {"message": "Some error occured"}
    else:
        return {"message": "Method not allowed"}

# Route to create a new task
@app.route("/create", methods=["POST"])
def create_taks():
    if request.method == "POST":
        request_data = request.get_json()
        name = request_data["name"]
        is_completed = request_data["is_completed"]
        try:
            data = TasksDB(name=name, is_completed=is_completed)
            session.add(data)
            session.commit()
            message = f"Task: {name} created successfully!"
            return {
                "message": message,
                "data": {
                    "id": data.id,
                    "name": data.name,
                    "is_completed": data.is_completed,
                },
            }
        except:
            return {"message": "Error while creating a task"}
    else:
        return {"message": "Method not allowed"}

# Route to update a task
@app.route("/update/<int:task_id>", methods=["PATCH"])
def update_task(task_id: int):
    if request.method == "PATCH":
        data = session.query(TasksDB).filter(TasksDB.id == task_id).first()
        if data is None:
            return {"message": f"Task with id: {task_id} does not exist."}
        else:
            request_data = request.get_json()
            is_completed = request_data["is_completed"]
            updated_data = {
                "id": task_id,
                "name": f"{data.name}",
                "is_completed": is_completed,
            }
            try:
                session.query(TasksDB).filter(TasksDB.id == task_id).update(
                    {"is_completed": is_completed}
                )
                session.commit()
                return {
                    "message":f"Task with id: {task_id} updated successfully.",
                    "data":updated_data
                }
            except:
                return {"message": f"Could not update the task with id: {task_id}"}
    else:
        return {"message": "Method not allowed"}


# Route to delete a task
@app.route("/delete/<int:task_id>", methods=["DELETE"])
def delete_task(task_id: int):
    if request.method == "DELETE":
        task = session.query(TasksDB).filter(TasksDB.id == task_id).first()
        if task is None:
            return {"message": f"Task with is: {task_id} does not exist."}
        else:
            try:
                session.delete(task)
                session.commit()
                return {"message": "Task deleted successfully"}
            except:
                return {"message": f"Couldn't delete the task with id: {task_id}"}
    else:
        return {"message": "Method not allowed"}


models.Base.metadata.create_all(engine)


if __name__=="__main__":
    app.run()