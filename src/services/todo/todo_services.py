
from src.entities import TodoEntity
from src.repository import TodoRepository


class TodoService:
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    def get_all_todos(self):
        return self.todo_repository.find_all()

    def get_all_todos_completed(self):
        return self.todo_repository.find_all_completed()

    def get_all_by_user_id(self, user_id):
        return self.todo_repository.find_all_by_user_id(user_id)

    def create_todo(self, todo: TodoEntity):
        return self.todo_repository.create_todo(todo)
