import os

FILENAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks


def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_tasks(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task cannot be empty!")



def view_tasks(tasks):
        if not tasks:
            print("📋 No tasks found.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")


def delete_tasks(tasks):
        view_tasks(tasks)
        if tasks:
            try:
                choice = int(input("Enter a task number to delete: "))
                if 1 <= choice <= len(tasks):
                    removed_task = tasks.pop(choice - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Task '{removed_task}' deleted successfully!")
                else:
                    print("⚠️ Invalid task number!")
            except ValueError:
                print("⚠️ Please enter a valid number!")


    
def main():
        tasks = load_tasks()

        while True:
            print("\nTo-Do List Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                add_tasks(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                delete_tasks(tasks)
            elif choice == "4":
                print("👋Exiting... Goodbye!")
                break
            else:
                print("⚠️ Invalid choice! Please try again.")


    

if __name__ == "__main__":
        main()

    
    