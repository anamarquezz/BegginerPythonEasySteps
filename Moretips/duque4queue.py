from collections import deque
queue = deque(['Zero', 'One', 'Two'])
print(queue.pop())
queue.append('Three')
queue = deque(['Zero', 'One', 'Three'])
queue.append('Four') #add
queue.append('Five')
queue.appendleft('Minus One')
print(queue)
print(queue.pop())  # remove the right
print(queue)
print(queue.popleft())  # remove the left
print(queue)
