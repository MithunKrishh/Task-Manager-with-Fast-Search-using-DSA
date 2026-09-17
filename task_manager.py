
class Task:
    def __init__(self, task_id, name, priority, status):
        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.status = status
        self.next = None


class TaskManager:

    def __init__(self):
        self.head = None


    def add_task(self, task_id, name, priority, status):

        current = self.head

        while current is not None:
            if current.task_id == task_id:
                print("Task ID already exists.")
                return

            current = current.next

        new_task = Task(task_id, name, priority, status)

        if self.head is None:
            self.head = new_task

        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_task

        print("Task added successfully.")



    def delete_task(self, task_id):

        if self.head is None:
            print("No tasks available.")
            return

        if self.head.task_id == task_id:
            self.head = self.head.next
            print("Task deleted successfully.")
            return

        current = self.head

        while current.next is not None:

            if current.next.task_id == task_id:

                current.next = current.next.next

                print("Task deleted successfully.")
                return

            current = current.next

        print("Task not found.")



    def update_status(self, task_id, new_status):

        current = self.head

        while current is not None:

            if current.task_id == task_id:

                current.status = new_status

                print("Task status updated successfully.")
                return

            current = current.next

        print("Task not found.")



    def display_tasks(self):

        if self.head is None:
            print("No tasks available.")
            return

        current = self.head

        print("\n----- All Tasks -----")

        while current is not None:

            print(
                "ID:", current.task_id,
                "| Name:", current.name,
                "| Priority:", current.priority,
                "| Status:", current.status
            )

            current = current.next



def main():

    manager = TaskManager()

    while True:

        print("\n========== TASK MANAGER ==========")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task Status")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            task_id = int(input("Enter Task ID: "))
            name = input("Enter Task Name: ")
            priority = input("Enter Priority (High/Medium/Low): ")
            status = input("Enter Status (Pending/In Progress/Done): ")

            manager.add_task(
                task_id,
                name,
                priority,
                status
            )

        elif choice == "2":

            task_id = int(input("Enter Task ID to delete: "))

            manager.delete_task(task_id)

        elif choice == "3":

            task_id = int(input("Enter Task ID: "))
            new_status = input(
                "Enter New Status (Pending/In Progress/Done): "
            )

            manager.update_status(task_id, new_status)

        elif choice == "4":

            manager.display_tasks()

        elif choice == "5":

            print("Exiting Task Manager...")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()