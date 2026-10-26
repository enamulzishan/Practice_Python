print("Welcome to my Simple To-Do list.")

todo_db = []
counter_id = 1

def add_task(task):
    global counter_id
    todo_db.append({"id": counter_id, "task": task})
    print(f"Task added with ID: {counter_id}")
    counter_id += 1

def view_tasks():
    if not todo_db:
        print("No tasks in the list.")
    else:
        for task in todo_db:
            print(f"ID: {task['id']}, Task: {task['task']}")

def delete_task(task_id):
    global todo_db
    todo_db = [task for task in todo_db if task['id'] != task_id]
    print(f"Task with ID: {task_id} has been deleted.")

def update_task(task_id, new_task):
    for task in todo_db:
        if task['id'] == task_id:
            task['task'] = new_task
            print(f"Task with ID: {task_id} has been updated.")
            return
    print(f"No task found with ID: {task_id}")
def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter the task ID to update: "))
            new_task = input("Enter the new task: ")
            update_task(task_id, new_task)
        elif choice == '5':
            print("Exiting the To-Do list.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()