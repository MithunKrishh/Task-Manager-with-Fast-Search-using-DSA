# Task Manager - Day 1 Demo

## 1. Project Introduction

This project is a console-based Student Task Manager developed in Python.

The Day 1 version focuses on implementing the task system using a custom Linked List.

Each task contains:

* Task ID
* Task Name
* Priority
* Status

The application supports adding, deleting, updating, and displaying tasks.

---

## 2. Demo Steps

### Step 1: Start the Program

Run:

```bash
python task_manager.py
```

The menu appears:

```text
========== TASK MANAGER ==========
1. Add Task
2. Delete Task
3. Update Task Status
4. Display Tasks
5. Exit
```

---

### Step 2: Add Tasks

Select option `1`.

Add:

```text
ID: 1
Name: Complete Assignment
Priority: High
Status: Pending
```

Then add:

```text
ID: 2
Name: Practice DSA
Priority: Medium
Status: Done
```

Then add:

```text
ID: 3
Name: Read Chapter 5
Priority: Low
Status: Pending
```

---

### Step 3: Display Tasks

Select option `4`.

Expected:

```text
========== ALL TASKS ==========
ID: 1 | Name: Complete Assignment | Priority: High | Status: Pending
ID: 2 | Name: Practice DSA | Priority: Medium | Status: Done
ID: 3 | Name: Read Chapter 5 | Priority: Low | Status: Pending
===============================
```

Explain:

> "The tasks are stored as nodes in a Linked List. The head points to the first node, and every node contains a reference to the next node."

---

### Step 4: Update Status

Select option `3`.

Enter:

```text
Task ID: 1
New Status: Done
```

Expected:

```text
Task status updated successfully.
```

Display the tasks again to verify the change.

---

### Step 5: Delete a Task

Select option `2`.

Enter:

```text
Task ID: 2
```

Expected:

```text
Task deleted successfully.
```

Display the tasks again.

The list should now contain:

```text
Task 1 -> Task 3 -> None
```

---

### Step 6: Demonstrate an Edge Case

Try deleting a task that does not exist:

```text
Task ID: 100
```

Expected:

```text
Task not found.
```

Then try adding Task ID `1` again.

Expected:

```text
Task ID already exists.
```

---

## 3. Short Explanation for the Demo

The main DSA concept demonstrated in this version is a Linked List.

Each task is a node.

```text
HEAD
 |
 v
Task 1 -> Task 2 -> Task 3 -> None
```

The `next` variable connects one task to the next task.

For adding a task, the program traverses to the end of the list and attaches the new node.

For deleting a task, the program changes the `next` reference so that the deleted node is skipped.

For updating a task, the program traverses the list until it finds the matching Task ID.

For displaying tasks, the program traverses every node from the head to `None`.

---

## 4. Viva Questions

### Q1. What data structure did you use?

**Answer:**

I used a singly Linked List to store the tasks.

### Q2. What does each node contain?

**Answer:**

Each node contains Task ID, Task Name, Priority, Status, and a reference to the next node.

### Q3. What is the purpose of `head`?

**Answer:**

`head` stores the reference to the first node in the Linked List.

### Q4. What does `next` store?

**Answer:**

`next` stores the reference to the next node.

### Q5. What happens when the list is empty?

**Answer:**

The `head` is `None`, so there are no nodes to traverse.

### Q6. How do you delete the first node?

**Answer:**

We move the head to the second node using:

```python
self.head = self.head.next
```

### Q7. What is the complexity of displaying all tasks?

**Answer:**

O(n), because every node has to be visited.

### Q8. What is the complexity of searching for a task?

**Answer:**

O(n) in the worst case because we may need to traverse the entire Linked List.

### Q9. Why did you use a Linked List?

**Answer:**

The project requires a Linked List for task management and traversal. It also allows me to demonstrate nodes, references, insertion, deletion, and traversal.

### Q10. What will you add in the next stage?

**Answer:**

In Day 2, I will add hashing for fast Task ID lookup and Binary Search for task-name searching. Recursion will be added in Day 3.
