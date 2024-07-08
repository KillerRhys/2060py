""" CLI-To-Do List
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.07.07(1638) """

# Variables
todo_list = []
fin_list = []
is_running = True

# Get saved data / create files on first run.
with open("data/todo.dat", "w+") as todo_file:
    things = todo_file.readlines()
    for item in things:
        todo_list.append(item)

with open("data/fin.dat", "w+") as fin_file:
    completed = fin_file.readlines()
    for item in completed:
        fin_list.append(item)


def show_items():
    my_lists = [todo_list, fin_list]
    for li in my_lists:
        if my_lists.index(li) == 0:
            print(f"\nTodo List: ")

        elif my_lists.index(li) == 1:
            print(f"\nCompleted Tasks: ")

        for i, j in enumerate(li):
            print(f'{i}-{j}')


# main logic.
while is_running:
    user_operation = input("Please enter a command, Add, Show, Edit, Delete, Complete: ")

    match user_operation.title():

        case "Add":
            new_item = input("What would you like to add? ")
            todo_list.append(new_item)

        case "Show":
            show_items()

        case "Edit":
            show_items()

            edit_item = input("Which item would you like to edit?")
            if len(todo_list) >= int(edit_item):
                update_item = input("Please type you edits: ")
                todo_list[int(edit_item)] = update_item

            else:
                print("That's not a valid selection!")

        case "Delete":
            show_items()

            target_item = input("Select item to delete: ")
            if len(todo_list) >= int(target_item):
                todo_list.pop(int(target_item))

        case "Complete":
            show_items()

            fin_item = input("Which item would you like to check off?")
            if len(todo_list) >= int(fin_item):
                fin_list.append(todo_list[int(fin_item)])
                todo_list.pop(int(fin_item))

        case "Exit":
            exit()
