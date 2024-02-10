from sys import stderr

import requests


class ApiService:
    def __init__(self):
        self.api = "https://jsonplaceholder.typicode.com/todos/"

    def get_all_todos(self):
        response = requests.get(self.api)
        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

    def run(self):
        print('Running ApiService', file=stderr)

        # TODO: follow README.md instructions
