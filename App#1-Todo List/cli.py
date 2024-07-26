""" CLI-To-Do List
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.07.07(1638) """

# Variables
todo_list = []
fin_list = []
is_running = True


def load_data():
    # Get saved data / create files on first run.
    try:
        with open("data/todo.dat", "r+") as todo_file:
            things = todo_file.readlines()
            for line in things:
                todo_list.append(f"{line.strip("\n")}")
    except FileNotFoundError:
        with open("data/todo.dat", "w+") as todo_file:
            todo_file.write("")
            print("File was created.")

    try:
        with open("data/fin.dat", "r+") as fin_file:
            completed = fin_file.readlines()
            for task in completed:
                fin_list.append(task.strip("\n"))
    except FileNotFoundError:
        with open("data/fin.dat", "w+") as fin_file:
            fin_file.write("")
            print("File was created")


# Save Data function
def save_data():
    with open("data/todo.dat", "w+") as todo_file:
        if not todo_list:
            pass
        else:
            for todo in todo_list:
                todo_file.write(f"{todo}\n")

    with open("data/fin.dat", "w+") as fin_file:
        if not fin_list:
            pass

        else:
            for completed_task in fin_list:
                fin_file.write(f"{completed_task}\n")


def show_items():
    my_lists = [todo_list, fin_list]
    for li in my_lists:
        if my_lists.index(li) == 0:
            print(f"\nTodo List: ")

        elif my_lists.index(li) == 1:
            print(f"\nCompleted Tasks: ")

        for i, j in enumerate(li):
            print(f'{i}-{j}')


# Build list or create files.
load_data()


# main logic.
while is_running:
    show_items()
    user_operation = input("Please enter a command, Add, Edit, Delete, Complete, Clear: ").title()

    if "Add" in user_operation:
        new_item = user_operation[4:]
        todo_list.append(new_item)
        print(f"{new_item} successfully added to list! \n")
        save_data()

    elif "Edit" in user_operation:
        try:
            edit_item = int(user_operation[5:])
            if len(todo_list) >= int(edit_item):
                before = todo_list[int(edit_item)]
                update_item = input("Please type you edits: ")
                after = update_item
                todo_list[int(edit_item)] = update_item
                print(f"Todo: {before}, was changed to {after}.\n")
                save_data()

            else:
                print("That's not a valid selection!")
        except ValueError:
            print("Incorrect command usage try 'Edit #' of the item you wish to edit.")

    elif "Delete" in user_operation:
        target_item = int(user_operation[7:])
        if len(todo_list) >= int(target_item):
            print(f"{todo_list[int(target_item)]} has been removed!\n")
            todo_list.pop(int(target_item))
            save_data()

    elif "Clear" in user_operation:
        for item in fin_list:
            fin_list.clear()

    elif "Complete" in user_operation:
        fin_item = int(user_operation[9:])
        if len(todo_list) >= int(fin_item):
            print(f"{todo_list[int(fin_item)]} has been checked off!\n")
            fin_list.append(todo_list[int(fin_item)])
            todo_list.pop(int(fin_item))
            save_data()

    elif "Exit" in user_operation:
        save_data()
        exit()

    else:
        print("Wrong selection! Try again..\n}")
