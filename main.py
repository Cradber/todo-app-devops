#!/usr/bin/env python

from src.controllers import AppController


app = AppController()

app.save_todos_as_csv()
