# Imports
from flask import Flask
import time
import json


# Vars
FILEPATH = "/Data/todo.json"
CURRENT_TIME = time.strftime("%Y.%B.%d - %H:%M:%S")
APP_INFO = """ 
               Get'R Done (To-Do App)
               Coded by TechGYQ
               www.mythosworks.com
               OC:2024.09.21(2118) 
            """


# TODO: Database creation & setup if not found.


# Main logic for all versions of app.
class Logic:
    def __init__(self):
        super(Logic).__init__()
        self.app = Flask(__name__)
        self.running = True
        self.todos = []
        self.complete = []

    # Prints app info.
    @staticmethod
    def app_info():
        print(APP_INFO)

    # TODO: Grab stored data for to-do's & completed tasks.
    def get_todos(self):
        for item in self.todos:
            print(item["start"], ":", item['name'], " Status:", item['status'] )

    # TODO: Write todos to db.
    def write_todos(self, todo):
        task = {
            "start": CURRENT_TIME,
            "name": todo,
            "status": False
        }
        self.todos.append(task)
