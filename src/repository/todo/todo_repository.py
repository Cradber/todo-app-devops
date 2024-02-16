from sqlalchemy.orm import Session

from src.entities import TodoEntity
from src.models import TodoModel


class TodoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find_all(self) -> [TodoEntity]:
        todos_model = self.db_session.query(TodoModel).all()
        return [self._map_model_to_entity(todo) for todo in todos_model]

    def find_all_completed(self) -> [TodoEntity]:
        return list(filter(lambda todo: todo.completed is True, self.find_all()))

    def find_all_uncompleted(self) -> [TodoEntity]:
        return list(filter(lambda todo: todo.completed is False, self.find_all()))

    def find_all_by_user_id(self, id: int) -> [TodoEntity]:
        return list(filter(lambda todo: todo.user_id == id, self.find_all()))

    def create_todo(self, todo_entity: TodoEntity):
        todo_model = TodoModel(user_id=todo_entity.user_id, title=todo_entity.title, completed=todo_entity.completed)
        self.db_session.add(todo_model)
        self.db_session.commit()
        return self._map_model_to_entity(todo_model)

    def _map_model_to_entity(self, todo_model: TodoModel) -> TodoEntity:
        return TodoEntity(user_id=todo_model.user_id, title=todo_model.title, completed=todo_model.completed)
