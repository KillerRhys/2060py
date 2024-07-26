""" Todo App Logic Class
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.07.26(1051) """


# Main logic class for all versions of app.
class Logic:
    def __init__(self):
        self.todos = []
        self.comps = []
        self.mylist = [self.todos, self.comps]
        self.is_running = True
        self.load_data()

    # Load function to grab previous data.
    def load_data(self):
        try:
            with open("data/todo.dat", "r+") as todo_file:
                things = todo_file.readlines()
                for line in things:
                    self.todos.append(f"{line.strip("\n")}")
        except FileNotFoundError:
            with open("data/todo.dat", 'w+') as todo_file:
                todo_file.write("")
                print("Missing file was created!")

        try:
            with open("data/fin.dat", "r+") as fin_file:
                completed = fin_file.readlines()
                for task in completed:
                    self.comps.append(task.strip("\n"))
        except FileNotFoundError:
            with open("data/fin.dat", "w+") as fin_file:
                fin_file.write("")
                print("Missing file was created!")

    # Save function to write all new todos to file.
    def save_data(self):
        with open("data/todo.dat", "w+") as todo_file:
            if not self.todos:
                pass
            else:
                for todo in self.todos:
                    todo_file.write(f"{todo}\n")

        with open("data/fin.dat", "w+") as fin_file:
            if not self.comps:
                pass
            else:
                for comp in self.comps:
                    fin_file.write(f"{comp}\n")

    # function to show items.
    def show_items(self):
        for li in self.mylist:
            if self.mylist.index(li) == 0:
                print(f"\nTodo List: ")

            elif self.mylist.index(li) == 1:
                print(f"\nCompleted Tasks: ")

            for i, j in enumerate(li):
                print(f"{i}-{j}")

    def add_item(self, user_operation):
        new_item = user_operation["Add ":]
        self.todos.append(new_item)
        print(f"{new_item} successfully added to list!\n")
        self.save_data()

    def edit_item(self, user_operation):
        try:
            edit_item = int(user_operation["Edit ":])
            if len[self.todos] >= edit_item:
                pass
