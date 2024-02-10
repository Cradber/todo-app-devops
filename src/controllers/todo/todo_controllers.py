from src.services import TodoService
from src.api import TodoAPIClient
from src.repository import TodoRepository


class TodoController:
    def __init__(self, api: str):
        api_client = TodoAPIClient(api)
        todo_repository = TodoRepository(api_client)
        self.todo_service = TodoService(todo_repository)

    def save_todos_as_csv(self):
        self.todo_service.save_todos_as_csv()
