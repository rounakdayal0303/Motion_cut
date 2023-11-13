class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self, new_task):
        self.tasks.append(new_task)
        print(f"Task '{new_task}' added to the to-do list.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task index. Please try again.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            to_do_list.show_tasks()
        elif choice == '2':
            new_task = input("Enter the new task: ")
            to_do_list.add_task(new_task)
        elif choice == '3':
            task_index = int(input("Enter the task index to remove: "))
            to_do_list.remove_task(task_index)
        elif choice == '4':
            print("Exiting the to-do list program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

