from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
task_id_counter = 1

# ROute 1: Listing all tasks
@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks), 200

# Route 2: Add a new task
@app.route('/tasks',methods=['POST'])
def add_task():
    global task_id_counter

    data = request.get_json()

    new_task = {
        "id": task_id_counter,
        "title": data.get("title","Untitled TAsk"),
        "status": "pending"
    }

    tasks.append(new_task)
    task_id_counter += 1

    return jsonify(new_task), 201

# Route 3: Mark a task as done
@app.route('/tasks/<int:task_id>/done', methods=['PUT'])

def mark_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            return jsonify(task), 200

    return jsonify({"error":"task not found"}), 404

# starting the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

