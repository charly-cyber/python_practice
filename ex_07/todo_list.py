tasks = []


def display_menu() -> None:
    print("\nTodo List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Edit task")
    print("4. Remove task")
    print("5. Exit")


def list_tasks() -> bool:
    if not tasks:
        print("No tasks available.")
        return False

    print("Your Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    return True


def add_task() -> None:
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task "{task}" added.')
    else:
        print("Empty task not added.")


def edit_task() -> None:
    if not list_tasks():
        return
    try:
        raw = input("Enter task index to edit: ").strip()
        if not raw:
            print("No index entered.")
            return
        task_index = int(raw) - 1
        if 0 <= task_index < len(tasks):
            current = tasks[task_index]
            new_value = input(f"Enter new description (leave empty to keep '{current}'): ").strip()
            if new_value:
                tasks[task_index] = new_value
                print("Task edited successfully.")
            else:
                print("Task unchanged.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")


def remove_task() -> None:
    if not list_tasks():
        return
    try:
        raw = input("Enter task index to remove: ").strip()
        if not raw:
            print("No index entered.")
            return
        task_index = int(raw) - 1
        if 0 <= task_index < len(tasks):
            removed = tasks.pop(task_index)
            print(f'Task "{removed}" deleted successfully.')
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")


def main() -> None:
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Exiting Todo List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    main()

