"""
CLI-To-Do List
Coded by TechGYQ
www.mythosworks.com
OC:2024.07.07(1638)
"""

# Imports
from logic import Logic

app = Logic()
app.load_data()


def print_help():
    print("\nAvailable Commands:")
    print("  Add [task]       : Add a new task")
    print("  Edit [index]     : Edit an existing task")
    print("  Delete [index]   : Delete a task")
    print("  Complete [index] : Mark a task as completed")
    print("  Clear            : Clear all tasks")
    print("  Exit             : Exit the application")
    print("  Help             : Show this help message\n")


def parse_command(user_operation):
    parts = user_operation.split(' ', 1)
    command = parts[0].capitalize()
    argument = parts[1] if len(parts) > 1 else None
    return command, argument


# Main logic
print_help()

while app.is_running:
    app.show_items()
    user_operation = input("Please enter a command: ").strip()
    command, argument = parse_command(user_operation)

    if command == "Add" and argument:
        app.add_item(argument)
    elif command == "Edit" and argument:
        try:
            index = int(argument.split(' ', 1)[0])
            app.edit_item(index, argument.split(' ', 1)[1])
        except (ValueError, IndexError):
            print("Invalid format for Edit. Use: Edit [index] [new task]")
    elif command == "Delete" and argument:
        try:
            app.delete_item(int(argument))
        except ValueError:
            print("Invalid index for Delete. Use: Delete [index]")
    elif command == "Complete" and argument:
        try:
            app.complete_task(int(argument))
        except ValueError:
            print("Invalid index for Complete. Use: Complete [index]")
    elif command == "Clear":
        app.clear_items()
    elif command == "Exit":
        app.exit_app()
    elif command == "Help":
        print_help()
    else:
        print("Unknown command. Type 'Help' for a list of available commands.")
