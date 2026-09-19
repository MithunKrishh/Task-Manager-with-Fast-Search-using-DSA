# Project 3: Task Manager with Fast Search

## Day 1: Task System

## 1. Project Description

The Task Manager is a simple console-based Python application designed to help students manage their assignments and activities.

Each task contains four details:

* Task ID
* Task Name
* Priority
* Status

The Day 1 implementation focuses on creating the basic task management system using a custom Linked List.

The current version supports:

1. Add Task
2. Delete Task
3. Update Task Status
4. Display Tasks

The Linked List is used to store and traverse all tasks.

---

## 2. Objectives

The main objectives of Day 1 are:

* Create a task structure.
* Implement a custom Linked List.
* Add tasks to the Linked List.
* Delete tasks from the Linked List.
* Update the status of a task.
* Display all tasks by traversing the Linked List.
* Handle basic edge cases.

---

## 3. DSA Concept Used

### Linked List

A Linked List is used as the main data structure for storing tasks.

Each task is represented as a node.

Each node contains:

```text
Task ID
Task Name
Priority
Status
Next
```

The `next` field stores the reference to the next task.

The structure looks like:

```text
HEAD
 |
 v
+---------+     +---------+     +---------+
| Task 1  | --> | Task 2  | --> | Task 3  | --> None
+---------+     +---------+     +---------+
```

The `head` variable stores the first task in the Linked List.

---

## 4. Task Structure

The `Task` class represents one node of the Linked List.

```python
class Task:

    def __init__(self, task_id, name, priority, status):
        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.status = status
        self.next = None
```

For example:

```text
ID       : 1
Name     : Complete Assignment
Priority : High
Status   : Pending
Next     : Next Task
```

---

## 5. Operations

### 5.1 Add Task

The `add_task()` function creates a new task node and adds it to the end of the Linked List.

Before adding the task, the program checks whether the Task ID already exists.

Example:

```text
1
Complete Assignment
High
Pending
```

The new node is added to the list.

### 5.2 Delete Task

The `delete_task()` function searches for a Task ID and removes the corresponding node.

There are two cases:

1. The task is the first node.
2. The task is somewhere after the first node.

When deleting a node, the previous node's `next` reference is changed to skip the deleted node.

Example:

```text
Before:

Task 1 -> Task 2 -> Task 3 -> None

Delete Task 2:

Task 1 ------------> Task 3 -> None
```

### 5.3 Update Task Status

The `update_status()` function searches for the Task ID.

When the task is found, its status is changed.

Example:

```text
Pending -> Done
```

### 5.4 Display Tasks

The `display_tasks()` function starts at the `head` and traverses the Linked List until it reaches `None`.

Example:

```text
HEAD
 |
 v
Task 1 -> Task 2 -> Task 3 -> None
```

Every task is printed during traversal.

---

## 6. Algorithm Approach

### Add Task

1. Start from the head.
2. Check whether the Task ID already exists.
3. Create a new Task node.
4. If the list is empty, make the new node the head.
5. Otherwise, traverse to the last node.
6. Connect the last node to the new node.

### Delete Task

1. Check whether the list is empty.
2. Check whether the head contains the requested ID.
3. If yes, move the head to the next node.
4. Otherwise, traverse the list.
5. Find the node whose next node contains the requested ID.
6. Skip that node.
7. If the ID is not found, display an error message.

### Update Status

1. Start from the head.
2. Traverse the list.
3. Compare each Task ID with the requested ID.
4. If found, update its status.
5. If not found, display an error message.

### Display Tasks

1. Start from the head.
2. Check whether the list is empty.
3. Print the current task.
4. Move to the next node.
5. Continue until `None`.

---

## 7. Complexity Analysis

Let `n` be the number of tasks.

| Operation     | Time Complexity | Space Complexity |
| ------------- | --------------: | ---------------: |
| Add Task      |            O(n) |             O(1) |
| Delete Task   |            O(n) |             O(1) |
| Update Status |            O(n) |             O(1) |
| Display Tasks |            O(n) |             O(1) |

### Explanation

**Add Task:**
The program traverses the list to check for duplicate IDs and then reaches the last node. Therefore, the worst-case time complexity is O(n).

**Delete Task:**
The program may need to search the entire list for the requested ID. Therefore, the worst-case complexity is O(n).

**Update Status:**
The program searches the list for the Task ID, so the worst-case complexity is O(n).

**Display Tasks:**
Every node must be visited, giving O(n).

---

## 8. Edge Cases

The following cases are handled:

### Empty Linked List

If there are no tasks:

```text
No tasks available.
```

### Duplicate Task ID

If the user tries to add an existing Task ID:

```text
Task ID already exists.
```

### Delete Missing Task

If the requested Task ID does not exist:

```text
Task not found.
```

### Update Missing Task

If the requested Task ID does not exist:

```text
Task not found.
```

### Delete First Node

The program correctly updates the `head` when the first task is deleted.

### Delete Last Node

The previous node is connected to `None`.

---

## 9. Example Data

The following data can be used for testing:

| ID | Task Name           | Priority | Status  |
| -: | ------------------- | -------- | ------- |
|  1 | Complete Assignment | High     | Pending |
|  2 | Practice DSA        | Medium   | Done    |
|  3 | Read Chapter 5      | Low      | Pending |

---

## 10. How to Run

Make sure Python is installed.

Open the terminal in the project directory and run:

```bash
python task_manager.py
```

The program will display:

```text
========== TASK MANAGER ==========
1. Add Task
2. Delete Task
3. Update Task Status
4. Display Tasks
5. Exit
```

Enter the corresponding number to perform an operation.

---

## 11. Current Project Scope

This is the Day 1 implementation.

Future stages will add:

### Day 2

* Hashing for Task ID lookup
* Sorted task-name collection
* Binary Search for task-name lookup

### Day 3

* Recursive pending-task counting
* Recursive condition-based search
* Additional testing
* Final complexity analysis
* Final demonstration

---

## 12. Conclusion

The Day 1 Task Manager successfully implements a basic task management system using a custom Linked List.

The project demonstrates how tasks can be represented as nodes and connected using references. It also implements insertion, deletion, updating, and traversal operations.

## Demo video:
https://drive.google.com/file/d/15QRANzehMzB5ChC1PZjsSoc2nMMH6g80/view?usp=sharing

The implementation provides the foundation for adding Hashing, Binary Search, and Recursion in the next stages of the project.
