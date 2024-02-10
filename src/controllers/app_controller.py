from src.controllers import TodoController


class AppController:
    def __init__(self):
        api = "https://jsonplaceholder.typicode.com/todos/"
        self.todo_controller = TodoController(api)

    def save_todos_as_csv(self) -> None:
        return self.todo_controller.save_todos_as_csv()
