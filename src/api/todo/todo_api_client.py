import requests


class TodoAPIClient:
    def __init__(self, url: str):
        self.api = url

    def fetch_todos(self):
        response = requests.get(self.api)

        return response.json() if response.ok else response.raise_for_status()
