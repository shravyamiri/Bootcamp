from collections import deque

# Stack (LIFO)
stack = deque()
stack.append("first")
stack.append("second")
print("Stack:", stack.pop(), stack.pop())
# Output: second first

# Queue (FIFO)
queue = deque()
queue.appendleft("first")
queue.appendleft("second")
print("Queue:", queue.pop(), queue.pop())
# Output: first second
