import sys

import heapq

N = int(sys.stdin.readline())

min_heap = []
max_heap = [] 

for n in range(1,N+1):
    value = int(sys.stdin.readline())
    if(n%2 == 1):
        heapq.heappush(max_heap, (-value,value))
    else:
        heapq.heappush(min_heap, value)

    if(n > 1 and max_heap[0][1] > min_heap[0]):
        tmp1 = heapq.heappop(max_heap)[1]
        tmp2 = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-tmp2,tmp2))
        heapq.heappush(min_heap, tmp1)

    print(max_heap[0][1])
