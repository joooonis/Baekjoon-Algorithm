from collections import deque
import sys


n = int(sys.stdin.readline())

queue = deque([ i for i in range(1,n+1) ])


for _ in range(n-1):
    queue.popleft()
    queue.rotate(-1)

print(queue.pop())
    
