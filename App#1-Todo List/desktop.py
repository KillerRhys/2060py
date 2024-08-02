""" Todo App Desktop Version
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.08.01(2200) """


import tkinter as tk
from tkinter import messagebox
from logic import Logic


class TodoApp:
    def __init__(self, root, logic):
        self.logic = logic
        self.root = root
        self.root.title("To-Do List")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, height=15, width=50, bd=0)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.complete_button = tk.Button(self.button_frame, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=10)

        self.load_tasks()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.logic.add_item(task)
            self.entry.delete(0, tk.END)
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            task_id = self.listbox.get(task_index).split(" - ")[0]
            self.logic.delete_item(int(task_id))
            self.load_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def complete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            task_id = self.listbox.get(task_index).split(" - ")[0]
            self.logic.complete_task(int(task_id))
            self.load_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def load_tasks(self):
        self.listbox.delete(0, tk.END)
        self.logic.load_data()  # Reload data from the database
        for task in self.logic.todos:
            self.listbox.insert(tk.END, f"{task.id} - {task.description}")
        for task in self.logic.comps:
            self.listbox.insert(tk.END, f"{task.id} - {task.description}")


if __name__ == "__main__":
    root = tk.Tk()
    logic = Logic()
    app = TodoApp(root, logic)
    root.mainloop()
