import datetime

class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.datetime.now()

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due = f"Due: {self.due_date.strftime('%Y-%m-%d')}" if self.due_date else "No due date"
        return f"[{status}] {self.description} ({due})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        task = Task(description, due_date)
        self.tasks.append(task)
        print(f"Task added: {task.description}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def complete_task(self, index):
        try:
            self.tasks[index - 1].mark_complete()
            print(f"Task {index} marked as complete.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, index):
        try:
            task = self.tasks.pop(index - 1)
            print(f"Task deleted: {task.description}")
        except IndexError:
            print("Invalid task number.")

    def view_task(self, index):
        try:
            task = self.tasks[index - 1]
            print(task)
        except IndexError:
            print("Invalid task number.")

def main():
    manager = TaskManager()
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. View Task")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
            manager.add_task(description, due_date)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            index = int(input("Enter task number to complete: "))
            manager.complete_task(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            manager.delete_task(index)
        elif choice == "5":
            index = int(input("Enter task number to view: "))
            manager.view_task(index)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
