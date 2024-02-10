from sys import stderr


class ApiService:
    def __init__(self):
        self.api = "https://jsonplaceholder.typicode.com/todos/"

    def run(self):
        print('Running ApiService', file=stderr)

        # TODO: follow README.md instructions
