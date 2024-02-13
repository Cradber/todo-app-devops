from dataclasses import dataclass


@dataclass
class TodoEntity:
    user_id: int
    title: str
    completed: bool = False

    def mark_as_completed(self) -> None:
        self.completed = True
