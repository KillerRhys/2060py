""" Todo App Logic
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.07.18(1600) """

import os


class Logic:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.todo_file = os.path.join(self.data_dir, "todo.dat")
        self.fin_file = os.path.join(self.data_dir, "fin.dat")
        self.todos = []
        self.comps = []
        self.mylist = [self.todos, self.comps]
        self.is_running = True
        self.load_data()

    def load_data(self):
        os.makedirs(self.data_dir, exist_ok=True)

        try:
            with open(self.todo_file, "r") as todo_file:
                self.todos = [line.strip() for line in todo_file.readlines()]
        except FileNotFoundError:
            with open(self.todo_file, 'w') as todo_file:
                todo_file.write("")  # Create the file if it doesn't exist
            print("Missing todo file was created!")

        try:
            with open(self.fin_file, "r") as fin_file:
                self.comps = [line.strip() for line in fin_file.readlines()]
        except FileNotFoundError:
            with open(self.fin_file, "w") as fin_file:
                fin_file.write("")  # Create the file if it doesn't exist
            print("Missing fin file was created!")

    def save_data(self):
        with open(self.todo_file, "w") as todo_file:
            for todo in self.todos:
                todo_file.write(f"{todo}\n")

        with open(self.fin_file, "w") as fin_file:
            for comp in self.comps:
                fin_file.write(f"{comp}\n")

    def show_items(self):
        print("\nTodo List:")
        for i, todo in enumerate(self.todos):
            print(f"{i} - {todo}")

        print("\nCompleted Tasks:")
        for i, comp in enumerate(self.comps):
            print(f"{i} - {comp}")

    def add_item(self, new_item):
        self.todos.append(new_item)
        print(f"{new_item} successfully added to list!\n")
        self.save_data()

    def edit_item(self, index, update_item):
        try:
            before = self.todos[index]
            self.todos[index] = update_item
            print(f"{before} was changed to {update_item}.\n")
            self.save_data()
        except IndexError:
            print("That is not a valid selection!")

    def delete_item(self, index):
        try:
            print(f"{self.todos[index]} has been removed!")
            self.todos.pop(index)
            self.save_data()
        except IndexError:
            print("That is not a valid selection!")

    def clear_items(self):
        self.todos.clear()
        self.comps.clear()
        self.save_data()
        print("All lists have been cleared!")

    def complete_task(self, index):
        try:
            print(f"{self.todos[index]} has been completed!\n")
            self.comps.append(self.todos[index])
            self.todos.pop(index)
            self.save_data()
        except IndexError:
            print("That is not a valid selection!")

    def exit_app(self):
        self.save_data()
        self.is_running = False
