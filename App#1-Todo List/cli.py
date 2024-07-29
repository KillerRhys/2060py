""" CLI-To-Do List
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.07.07(1638) """

# Imports
from logic import Logic
app = Logic()
app.load_data()

# main logic.
while app.is_running:
    app.show_items()
    user_operation = input("Please enter a command, Add, Edit, Delete, Complete, Clear: ").title()

    if "Add" in user_operation:
        app.add_item(user_operation)

    elif "Edit" in user_operation:
        app.edit_item(user_operation)

    elif "Delete" in user_operation:
        app.delete_item(user_operation)

    elif "Clear" in user_operation:
        app.clear_items()

    elif "Complete" in user_operation:
        app.complete_task(user_operation)

    elif "Exit" in user_operation:
        app.exit_app()

    else:
        print("Wrong selection! Try again..\n}")
