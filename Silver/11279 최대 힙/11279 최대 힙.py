from heapq import heappush, heappop
import sys

heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0 and not heap:
        print(0)
    elif x == 0:
        print(heappop(heap)[1])
    else:
        heappush(heap, (-x, x))
