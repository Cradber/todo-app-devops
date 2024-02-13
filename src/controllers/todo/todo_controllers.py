from src.entities import TodoEntity
from src.models.todo import get_db
from src.services import TodoService
# from src.api import TodoAPIClient
from src.repository import TodoRepository


class TodoController:
    def __init__(self):
        # api_client = TodoAPIClient()
        # todo_repository = TodoRepository(api_client)
        self.db_session = get_db()
        todo_repository = TodoRepository(self.db_session)
        self.todo_service = TodoService(todo_repository)

    def get_todos(self) -> [TodoEntity]:
        todos = self.todo_service.get_all_todos()
        self.db_session.close()
        return todos

    def get_todo_by_user_id(self, user_id: int) -> [TodoEntity]:
        todos = self.todo_service.get_all_by_user_id(user_id)
        self.db_session.close()
        return todos

    def create_todo(self, todo: TodoEntity) -> TodoEntity:
        return self.todo_service.create_todo(todo)
