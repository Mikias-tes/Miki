tasks = []

def add_task():
    task = input("Enter the task that you want to add: ")
    tasks.append(task)

def remove_task():
    task = input("Enter the task that you want to remove: ")
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found.")

def clear_tasks():
    tasks.clear()

while True:
    print("1 add task")
    print("2 remove task")
    print("3 clear tasks")

    choice = input("choose from 1 2 3: ") 

    if choice == "1":
        add_task()
        print(tasks)
    elif choice == "2":
        remove_task()
        print(tasks)
    elif choice == "3":
        clear_tasks()
        print(tasks)
    else:
        print("invalid")

     