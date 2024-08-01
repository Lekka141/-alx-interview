# 0x01. Lockboxes

## Overview

This project requires developing a solution to determine if all lockboxes can be opened. You will use various algorithmic concepts and Python programming skills to achieve this.

## Concepts Needed

### Lists and List Manipulation
- Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
- [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

### Graph Theory Basics
- Knowledge of graph theory, especially traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS), can be helpful.
- [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms)

### Algorithmic Complexity
- Understanding the time and space complexity of your solution is important for writing efficient algorithms.
- [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

### Recursion
- Some solutions might require a recursive approach to traverse through the boxes and keys.
- [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

### Queue and Stack
- Using queues and stacks is crucial for implementing BFS or DFS algorithms.
- [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/stack-in-python/)

### Set Operations
- Using sets to keep track of visited boxes and available keys can optimize the search process.
- [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

### Additional Resources
- [Mock Technical Interview](https://www.interviewbit.com/mock-interview/)

## Requirements

- **Allowed editors**: vi, vim, emacs
- **Interpreter/Compiler**: All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Ending**: All files should end with a new line
- **First Line**: The first line of all files should be exactly `#!/usr/bin/python3`
- **README.md**: A `README.md` file at the root of the project folder is mandatory
- **Documentation**: Your code should be documented
- **Code Style**: Your code should use the PEP 8 style (version 1.7.x)
- **Executable Files**: All files must be executable

## Tasks

### 0. Lockboxes
**Mandatory**

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- **Prototype**: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

Example:

```python
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False

carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
