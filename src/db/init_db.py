# src/init_db.py
import json

from src.models import TodoModel
from src.models.todo import Base, engine, SessionLocal


def create_tables():
    Base.metadata.create_all(bind=engine)


def init_db():
    # with open('todos.json', 'r') as file:
    with open('/app/src/todos.json', 'r') as file:
        data = json.load(file)

    session = SessionLocal()

    for item in data:
        todo = TodoModel(
            user_id=item['userId'],
            title=item['title'],
            completed=item['completed']
        )
        session.add(todo)

    session.commit()
    print("Base de datos inicializada con éxito.")


if __name__ == "__main__":
    create_tables()
    init_db()
