from dataclasses import dataclass


@dataclass
class Todo:
    def __init__(self, user_id: int, title: str, completed: bool):
        self.id = user_id
        self.title = title
        self.completed = completed

    def mark_as_completed(self) -> None:
        self.completed = True
