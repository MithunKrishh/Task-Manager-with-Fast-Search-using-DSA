# Task Manager - Day 1 Test Cases

## Test Case 1: Add First Task

### Input

```text
Choice: 1
Task ID: 1
Task Name: Complete Assignment
Priority: High
Status: Pending
```

### Expected Output

```text
Task added successfully.
```

### Result

Pass

---

## Test Case 2: Add Multiple Tasks

### Input

```text
1 | Complete Assignment | High | Pending
2 | Practice DSA | Medium | Done
3 | Read Chapter 5 | Low | Pending
```

### Expected Output

All three tasks should be added successfully.

```text
Task added successfully.
Task added successfully.
Task added successfully.
```

### Result

Pass

---

## Test Case 3: Display Tasks

### Input

```text
Choice: 4
```

### Expected Output

```text
========== ALL TASKS ==========
ID: 1 | Name: Complete Assignment | Priority: High | Status: Pending
ID: 2 | Name: Practice DSA | Priority: Medium | Status: Done
ID: 3 | Name: Read Chapter 5 | Priority: Low | Status: Pending
===============================
```

### Result

Pass

---

## Test Case 4: Update Task Status

### Input

```text
Choice: 3
Task ID: 1
New Status: Done
```

### Expected Output

```text
Task status updated successfully.
```

### Verification

Display the tasks again.

Task 1 should show:

```text
Status: Done
```

### Result

Pass

---

## Test Case 5: Delete Middle Task

### Initial List

```text
Task 1 -> Task 2 -> Task 3 -> None
```

### Input

```text
Choice: 2
Task ID: 2
```

### Expected Output

```text
Task deleted successfully.
```

### Expected List

```text
Task 1 -> Task 3 -> None
```

### Result

Pass

---

## Test Case 6: Delete First Task

### Initial List

```text
Task 1 -> Task 2 -> Task 3 -> None
```

### Input

```text
Choice: 2
Task ID: 1
```

### Expected List

```text
Task 2 -> Task 3 -> None
```

### Result

Pass

---

## Test Case 7: Delete Last Task

### Initial List

```text
Task 1 -> Task 2 -> Task 3 -> None
```

### Input

```text
Choice: 2
Task ID: 3
```

### Expected List

```text
Task 1 -> Task 2 -> None
```

### Result

Pass

---

# Edge Cases

## Test Case 8: Empty Linked List

Start the program and select Display Tasks without adding anything.

### Input

```text
Choice: 4
```

### Expected Output

```text
No tasks available.
```

### Result

Pass

---

## Test Case 9: Add Duplicate Task ID

First add:

```text
ID: 1
Name: Complete Assignment
Priority: High
Status: Pending
```

Then try to add another task with:

```text
ID: 1
Name: Practice DSA
Priority: Medium
Status: Pending
```

### Expected Output

```text
Task ID already exists.
```

### Result

Pass

---

## Test Case 10: Delete Missing Task

### Input

```text
Choice: 2
Task ID: 100
```

### Expected Output

```text
Task not found.
```

### Result

Pass

---

## Test Case 11: Update Missing Task

### Input

```text
Choice: 3
Task ID: 100
New Status: Done
```

### Expected Output

```text
Task not found.
```

### Result

Pass

---

## Test Case 12: Delete From Empty List

Start the program without adding any task.

### Input

```text
Choice: 2
Task ID: 1
```

### Expected Output

```text
No tasks available.
```

### Result

Pass

---

## Test Case 13: Update From Empty List

Start the program without adding any task.

### Input

```text
Choice: 3
Task ID: 1
New Status: Done
```

### Expected Output

```text
Task not found.
```

### Result

Pass

---

## Test Case 14: Invalid Task ID

### Input

```text
Choice: 1
Task ID: abc
```

### Expected Output

```text
Task ID must be a number.
```

### Result

Pass

---

# Test Summary

| Test | Description         | Expected Result     | Status |
| ---- | ------------------- | ------------------- | ------ |
| 1    | Add first task      | Task added          | Pass   |
| 2    | Add multiple tasks  | Tasks added         | Pass   |
| 3    | Display tasks       | All tasks displayed | Pass   |
| 4    | Update status       | Status changed      | Pass   |
| 5    | Delete middle task  | Node removed        | Pass   |
| 6    | Delete first task   | Head updated        | Pass   |
| 7    | Delete last task    | Last node removed   | Pass   |
| 8    | Display empty list  | No tasks message    | Pass   |
| 9    | Duplicate ID        | Rejected            | Pass   |
| 10   | Delete missing task | Not found           | Pass   |
| 11   | Update missing task | Not found           | Pass   |
| 12   | Delete empty list   | No tasks message    | Pass   |
| 13   | Update empty list   | Not found           | Pass   |
| 14   | Invalid ID          | Input rejected      | Pass   |

Total Test Cases: **14**
