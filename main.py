from flask import Flask, jsonify, request

from src.controllers import TodoController
from src.entities import TodoEntity
from src.models.todo import DATABASE_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
todo_controller = TodoController()


@app.route('/', methods=['GET'])
def get_hello():
    # Use todo_controller to get todos and return them
    todos = "Welcome to the API"
    return jsonify(todos), 200


@app.route('/todos', methods=['GET'])
def get_todos():
    # Use todo_controller to get todos and return them
    todos = todo_controller.get_todos()
    return jsonify(todos), 200


@app.route('/todos/<int:user_id>', methods=['GET'])
def get_todos_by_user_id(user_id):
    # Use todo_controller to get todos and return them
    todos = todo_controller.get_todo_by_user_id(user_id)
    return jsonify(todos), 200


@app.route('/todos/<int:user_id>', methods=['POST'])
def create_todo(user_id):
    # Get the JSON data from the request
    todo_data = request.get_json()

    # You may want to validate the input data here
    if 'title' not in todo_data and 'completed' not in todo_data:
        return jsonify({'error': 'Missing title or completed status'}), 400

    # Use the todo_controller to add the new todo
    try:
        todo = TodoEntity(
            user_id=user_id,
            title=todo_data['title'],
            completed=todo_data['completed']
        )
        print(todo)
        created_todo = todo_controller.create_todo(todo)
        return jsonify(created_todo), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/todos/completed', methods=['GET'])
def get_todos_completed():
    # Use todo_controller to get todos and return them
    todos = todo_controller.get_todos_completed()
    return jsonify(todos), 200


@app.route('/todos/uncompleted', methods=['GET'])
def get_todos_completed():
    # Use todo_controller to get todos and return them
    todos = todo_controller.get_todos_uncompleted()
    return jsonify(todos), 200


# Add more routes for update and delete functionalities

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
