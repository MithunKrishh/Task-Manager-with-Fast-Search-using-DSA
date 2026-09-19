# Project 3: Task Manager
# Day 1 - Task System
# Linked List Implementation
#
# Features:
# 1. Add Task
# 2. Delete Task
# 3. Update Task Status
# 4. Display Tasks


# --------------------------------
# Task Node
# --------------------------------

class Task:

    def __init__(self, task_id, name, priority, status):
        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.status = status
        self.next = None


# --------------------------------
# Task Manager
# --------------------------------

class TaskManager:

    def __init__(self):
        self.head = None


    # --------------------------------
    # Add Task
    # --------------------------------

    def add_task(self, task_id, name, priority, status):

        # Check for duplicate Task ID
        current = self.head

        while current is not None:

            if current.task_id == task_id:
                print("Task ID already exists.")
                return

            current = current.next

        # Create a new task node
        new_task = Task(
            task_id,
            name,
            priority,
            status
        )

        # If linked list is empty
        if self.head is None:

            self.head = new_task

        else:

            # Traverse to the last node
            current = self.head

            while current.next is not None:
                current = current.next

            # Add new node at the end
            current.next = new_task

        print("Task added successfully.")


    # --------------------------------
    # Delete Task
    # --------------------------------

    def delete_task(self, task_id):

        # Check if list is empty
        if self.head is None:

            print("No tasks available.")
            return

        # Delete first node
        if self.head.task_id == task_id:

            self.head = self.head.next

            print("Task deleted successfully.")
            return

        # Search for the task
        current = self.head

        while current.next is not None:

            if current.next.task_id == task_id:

                # Remove the node
                current.next = current.next.next

                print("Task deleted successfully.")
                return

            current = current.next

        print("Task not found.")


    # --------------------------------
    # Update Task Status
    # --------------------------------

    def update_status(self, task_id, new_status):

        current = self.head

        while current is not None:

            if current.task_id == task_id:

                current.status = new_status

                print("Task status updated successfully.")
                return

            current = current.next

        print("Task not found.")


    # --------------------------------
    # Display Tasks
    # --------------------------------

    def display_tasks(self):

        # Check if list is empty
        if self.head is None:

            print("No tasks available.")
            return

        current = self.head

        print("\n========== ALL TASKS ==========")

        # Traverse the linked list
        while current is not None:

            print(
                "ID:", current.task_id,
                "| Name:", current.name,
                "| Priority:", current.priority,
                "| Status:", current.status
            )

            current = current.next

        print("===============================")


# --------------------------------
# Main Program
# --------------------------------

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

        # ----------------------------
        # Add Task
        # ----------------------------

        if choice == "1":

            try:
                task_id = int(input("Enter Task ID: "))
            except ValueError:
                print("Task ID must be a number.")
                continue

            name = input("Enter Task Name: ")

            priority = input(
                "Enter Priority (High/Medium/Low): "
            )

            status = input(
                "Enter Status (Pending/In Progress/Done): "
            )

            manager.add_task(
                task_id,
                name,
                priority,
                status
            )


        # ----------------------------
        # Delete Task
        # ----------------------------

        elif choice == "2":

            try:
                task_id = int(
                    input("Enter Task ID to delete: ")
                )
            except ValueError:
                print("Task ID must be a number.")
                continue

            manager.delete_task(task_id)


        # ----------------------------
        # Update Status
        # ----------------------------

        elif choice == "3":

            try:
                task_id = int(
                    input("Enter Task ID: ")
                )
            except ValueError:
                print("Task ID must be a number.")
                continue

            new_status = input(
                "Enter New Status (Pending/In Progress/Done): "
            )

            manager.update_status(
                task_id,
                new_status
            )


        # ----------------------------
        # Display Tasks
        # ----------------------------

        elif choice == "4":

            manager.display_tasks()


        # ----------------------------
        # Exit
        # ----------------------------

        elif choice == "5":

            print("Exiting Task Manager...")
            break


        else:

            print("Invalid choice. Please try again.")


# --------------------------------
# Program Starting Point
# --------------------------------

if __name__ == "__main__":
    main()