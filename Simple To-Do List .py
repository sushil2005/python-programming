

todo_list = []

def show_menu():
    print("\n📋 To-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("📝 No tasks yet!")
    else:
        print("📝 Your Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter task to add: ")
    todo_list.append(task)
    print(f"✅ Task '{task}' added!")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"❌ Task '{removed}' removed!")
            else:
                print("⚠️ Invalid task number!")
        except ValueError:
            print("⚠️ Please enter a number!")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:

            print("⚠️ Invalid option, try again!")
