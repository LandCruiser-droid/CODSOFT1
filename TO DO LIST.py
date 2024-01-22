import os
import pickle
from datetime import datetime

class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.completed = False
        self.creation_date = datetime.now()
        self.due_date = due_date

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} (Due: {self.due_date}) - {status} ({self.creation_date})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def save_to_file(self, filename="todolist.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.tasks, file)

    def load_from_file(self, filename="todolist.pkl"):
        if os.path.exists(filename):
            with open(filename, "rb") as file:
                self.tasks = pickle.load(file)


def main():
    todo_list = ToDoList()

    # Load tasks from file if exists
    todo_list.load_from_file()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Remove Task")
        print("4. List Tasks")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, format: YYYY-MM-DD): ")
            task = Task(description, due_date)
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            todo_list.list_tasks()
            index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= index < len(todo_list.tasks):
                todo_list.tasks[index].mark_as_completed()
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

        elif choice == "3":
            todo_list.list_tasks()
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(todo_list.tasks):
                removed_task = todo_list.tasks.pop(index)
                print(f"Task '{removed_task.description}' removed successfully!")
            else:
                print("Invalid task number.")

        elif choice == "4":
            todo_list.list_tasks()

        elif choice == "5":
            # Save tasks to file before exiting
            todo_list.save_to_file()
            print("Tasks saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
