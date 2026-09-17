# Project 3: Task Manager with Fast Search

## 1. Project Description

The Task Manager is a simple console-based Python application designed to help students manage their assignments and activities.

Each task contains:

* Task ID
* Task Name
* Priority
* Status

The application allows users to add, delete, update, display, and search tasks.

The main purpose of this project is to demonstrate the practical use of different Data Structures and Algorithms (DSA) concepts.

The DSA concepts used are:

1. Linked List
2. Hashing
3. Binary Search
4. Recursion

---

## 2. Features

The application provides the following operations:

1. Add a Task
2. Delete a Task by Task ID
3. Find a Task by Task ID
4. Find a Task by Task Name
5. Update Task Status
6. Display All Tasks
7. Count Pending Tasks Recursively
8. Find the First Task with a Given Priority Recursively
9. Exit

---

## 3. DSA Concepts Used

### 3.1 Linked List

A custom linked list is used to store and manage tasks.

Each task is represented as a node containing:

* Task ID
* Task Name
* Priority
* Status
* Reference to the next task

Example:

```text
HEAD
 |
 v
[Task 1] -> [Task 2] -> [Task 3] -> None
```

The linked list is traversed when displaying all tasks.

### Why Linked List?

The project specifically requires tasks to be stored and traversed using a linked list. It also provides practical experience with nodes, pointers/references, insertion, deletion, and traversal.

---

### 3.2 Hashing

A Python dictionary is used as a hash table for Task ID lookup.

```python
self.task_hash = {}
```

Each Task ID is mapped to its corresponding task node.

Example:

```text
1 -> Task 1
2 -> Task 2
3 -> Task 3
```

This allows a task to be found quickly using its ID.

### Why Hashing?

Task IDs are unique, making them suitable as hash keys.

The average time complexity for searching by ID is:

```text
O(1)
```

---

### 3.3 Binary Search

A separate collection of task nodes is maintained in sorted order by task name.

Binary Search is then used to find a task by its name.

The algorithm compares the search name with the middle element.

If the search name is smaller, the left half is searched.

If the search name is larger, the right half is searched.

Example:

```text
Complete Assignment
Practice DSA
Read Chapter 5
```

If searching for `Read Chapter 5`, binary search eliminates unnecessary elements instead of checking every task.

### Why Binary Search?

Binary search is much faster than linear search when the data is sorted.

Time complexity:

```text
O(log n)
```

---

### 3.4 Recursion

Recursion is used for two operations.

#### Count Pending Tasks

The program recursively traverses the linked list and counts tasks whose status is `Pending`.

Example:

```text
Task 1 -> Pending
Task 2 -> Done
Task 3 -> Pending
```

Result:

```text
2 pending tasks
```

#### Priority-Based Search

Recursion is also used to find the first task matching a selected priority.

For example:

```text
Search Priority: High
```

The program checks each linked-list node recursively until a matching task is found.

### Base Case

The base case occurs when the current node is `None`.

```python
if node is None:
    return 0
```

or:

```python
if node is None:
    return None
```

This stops the recursion when there are no more tasks.

---

# 4. Approach

The application maintains three structures:

```text
                  Task Manager
                       |
        +--------------+--------------+
        |              |              |
   Linked List     Hash Table     Sorted Collection
        |              |              |
   Store Tasks     ID Lookup       Name Search
        |              |              |
    O(n)            O(1)*          Binary Search
                                      O(log n)
```

### Adding a Task

1. Check whether the Task ID already exists.
2. Create a new task node.
3. Add the node to the linked list.
4. Add the task to the hash table.
5. Add the task to the sorted collection.
6. Sort the collection by task name.

### Deleting a Task

1. Check whether the Task ID exists.
2. Locate the corresponding node.
3. Remove it from the linked list.
4. Remove it from the hash table.
5. Remove it from the sorted collection.

### Finding by ID

The Task ID is used as a key in the hash table.

```text
Task ID -> Hash Table -> Task
```

### Finding by Name

The sorted task collection is searched using Binary Search.

### Updating Status

The hash table is used to locate the task quickly, and its status is modified.

### Displaying Tasks

The linked list is traversed from the head node until `None`.

### Counting Pending Tasks

The linked list is recursively traversed and every `Pending` task is counted.

---

# 5. Complexity Analysis

| Operation          | Technique                       | Time Complexity |
| ------------------ | ------------------------------- | --------------: |
| Add Task           | Linked List + Hashing + Sorting |           O(n²) |
| Delete Task        | Linked List + Hashing           |            O(n) |
| Find by ID         | Hashing                         |    O(1) average |
| Find by Name       | Binary Search                   |        O(log n) |
| Update Status      | Hashing                         |    O(1) average |
| Display Tasks      | Linked List                     |            O(n) |
| Count Pending      | Recursion                       |            O(n) |
| Search by Priority | Recursion                       |            O(n) |
| Sort Task Names    | Bubble Sort                     |           O(n²) |

`n` represents the number of tasks.

### Space Complexity

The application stores the tasks in multiple structures.

The overall additional space is:

```text
O(n)
```

because the linked list, hash table, and sorted collection each store references to the tasks.

---

# 6. Edge Cases Handled

The application handles the following edge cases:

### Empty Task List

If there are no tasks, displaying tasks produces:

```text
No tasks available.
```

### Duplicate Task ID

If a user enters an existing Task ID:

```text
Task ID already exists.
```

The task is not added.

### Missing Task ID

If a user searches for an ID that does not exist:

```text
Task not found.
```

### Deleting a Missing Task

If the user tries to delete a nonexistent task:

```text
Task not found.
```

### No Pending Tasks

The recursive pending counter returns:

```text
Number of pending tasks: 0
```

### All Tasks Pending

The recursive function counts every task and returns the total number of tasks.

### Duplicate Task Names

The program can store tasks with duplicate names. Binary Search returns a matching task if the searched name exists.

### Empty Linked List

The linked-list head is `None`, which is also the base case for recursive operations.

---

# 7. Example Tasks

The following tasks can be used during the demonstration:

| ID | Task Name           | Priority | Status  |
| -: | ------------------- | -------- | ------- |
|  1 | Complete Assignment | High     | Pending |
|  2 | Practice DSA        | Medium   | Done    |
|  3 | Read Chapter 5      | Low      | Pending |

---

# 8. How to Run

Make sure Python is installed.

Open the terminal in the project folder and run:

```bash
python task_manager.py
```

The program will display the main menu.

```text
========== TASK MANAGER ==========
1. Add Task
2. Delete Task
3. Find Task by ID
4. Find Task by Name
5. Update Task Status
6. Display All Tasks
7. Count Pending Tasks
8. Find Task by Priority
9. Exit
```

---

# 9. Conclusion

This project demonstrates how different DSA concepts can work together in a real-world application.

The Linked List manages the task collection, Hashing provides fast Task ID lookup, Binary Search provides efficient task-name searching, and Recursion is used for counting and condition-based searching.

The project also demonstrates handling common edge cases such as duplicate IDs, missing tasks, and an empty task list.
