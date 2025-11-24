tasks = {}

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        tasks[len(tasks)+1] = task
    elif choice == "2":
        for k, v in tasks.items():
            print(k, ":", v)
    elif choice == "3":
        break
    else:
        print("Invalid choice")