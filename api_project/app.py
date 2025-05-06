from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Estudar Cybersecurity", "done": False},
    {"id": 2, "task": "Desenvolver API", "done": False},
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = next((todo for todo in todos if todo['id'] == id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    
    todo.update(request.get_json())
    return jsonify(todo)

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo['id'] != id]
    return '', 204

import os

if __name__ == '__main__':
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode)

