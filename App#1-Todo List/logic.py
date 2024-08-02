""" Todo App Logic
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.07.18(1600) """


from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database
DATABASE_URL = "sqlite:///todo_app.db"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Define the base class
Base = declarative_base()


# Define the Todo model
class TodoItem(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)


# Create the tables in the database
# Base.metadata.create_all(engine)


class Logic:
    def __init__(self):
        self.session = session
        self.is_running = True
        self.todos = []
        self.comps = []

    def load_data(self):
        self.todos = self.session.query(TodoItem).filter_by(completed=False).all()
        self.comps = self.session.query(TodoItem).filter_by(completed=True).all()

    def save_data(self):
        self.session.commit()

    def show_items(self):
        print("\nTodo List:")
        for todo in self.todos:
            print(f"{todo.id} - {todo.description}")

        print("\nCompleted Tasks:")
        for comp in self.comps:
            print(f"{comp.id} - {comp.description}")

    def add_item(self, new_item):
        new_todo = TodoItem(description=new_item)
        self.session.add(new_todo)
        self.save_data()
        print(f"{new_item} successfully added to list!\n")
        self.load_data()

    def edit_item(self, index, update_item):
        try:
            todo = self.session.query(TodoItem).get(index)
            if todo and not todo.completed:
                before = todo.description
                todo.description = update_item
                self.save_data()
                print(f"{before} was changed to {update_item}.\n")
                self.load_data()
            else:
                print("That is not a valid selection or item is already completed!")
        except ValueError:
            print("That is not a valid selection!")

    def delete_item(self, index):
        try:
            todo = self.session.query(TodoItem).get(index)
            if todo:
                self.session.delete(todo)
                self.save_data()
                print(f"{todo.description} has been removed!")
                self.load_data()
            else:
                print("That is not a valid selection!")
        except ValueError:
            print("That is not a valid selection!")

    def clear_items(self):
        self.session.query(TodoItem).delete()
        self.save_data()
        self.load_data()
        print("All lists have been cleared!")

    def complete_task(self, index):
        try:
            todo = self.session.query(TodoItem).get(index)
            if todo and not todo.completed:
                todo.completed = True
                self.save_data()
                print(f"{todo.description} has been completed!\n")
                self.load_data()
            else:
                print("That is not a valid selection or item is already completed!")
        except ValueError:
            print("That is not a valid selection!")

    def exit_app(self):
        self.save_data()
        self.session.close()
        self.is_running = False
