from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)

print(list(dq))
# Output: [4, 5, 1, 2, 3]
