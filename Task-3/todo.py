'''Command-Line To-Do List Application
Description: A simple CLI app to manage tasks using  Python.'''

tasks = []

def show_menu():
    "Display menu"
    print("\n📝 TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📌 Your Tasks:")
    for idx,task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
              
def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num-1)
            print(f"🗑️ Task '{removed}' removed successfully!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Exiting TO-Do App. Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()