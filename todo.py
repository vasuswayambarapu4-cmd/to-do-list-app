#to do list python code 
tasks = []

def show_menu():
    print("\n--- TO-DO LIST APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("✔ Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("\nEnter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"✔ Deleted: {removed}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Enter a valid number!")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again!")
