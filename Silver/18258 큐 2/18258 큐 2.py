from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        queue.append(int(line[1]))
    elif line[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(queue))
    elif line[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif line[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif line[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
