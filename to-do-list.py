def main():
    tasks = []

    while True:
        print("\n*** To-Do List Menu ***")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks) # type: ignore
        elif choice == "2":
            view_tasks(tasks) # type: ignore
        elif choice == "3":
            mark_completed(tasks) # type: ignore
        elif choice == "4":
            delete_task(tasks) # type: ignore
        elif choice == "5":
            print("Exiting program...")
            break 
        else:
            print("Invalid choice. Please try again.")


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\n*** Tasks ***")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}, {task['task']} - {status}")


def mark_completed(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True 
            print("Task marked as completed.")
        else:
            print("Invalid Index.")
    except ValueError:
            print("Invalid input. Please enter a valid index. ")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


if __name__ == "__main__":
    main()