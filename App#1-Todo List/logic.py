# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import time


# Vars
CURRENT_TIME = time.strftime("%Y.%B.%d - %H:%M:%S")
APP_INFO = """ 
               Get'R Done (To-Do App)
               Coded by TechGYQ
               www.mythosworks.com
               OC:2024.09.21(2118) 
            """


# Database creation & setup if not found.
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    status: Mapped[bool]
    name: Mapped[str] = mapped_column(primary_key=True)
    begin: Mapped[str]
    finish: Mapped[str]


# Main logic for all versions of app.
class Logic(Flask):
    def __init__(self):
        super(Logic).__init__()
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Data/TODO.db"
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()
        self.todos = {}
        self.complete = {}

    # Prints app info.
    @staticmethod
    def app_info():
        print(APP_INFO)

    # Grab stored data for to-do's & completed tasks.

