# src/models/todo_model.py
import os

from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()


class TodoModel(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)


# DATABASE_URL = 'postgresql://user:password@localhost:5432/todosdb'
DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    return db
