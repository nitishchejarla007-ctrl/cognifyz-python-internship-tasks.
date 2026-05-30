tasks = []

while True:
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, task)

    elif choice == "3":
        for i, task in enumerate(tasks, start=1):
            print(i, task)

        num = int(input("Enter task number to update: "))
        tasks[num - 1] = input("Enter new task: ")
        print("Task Updated Successfully!")

    elif choice == "4":
        for i, task in enumerate(tasks, start=1):
            print(i, task)

        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task Deleted Successfully!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")