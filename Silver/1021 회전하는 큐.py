# Circular Queue
# %(moduler) 연산을 사용해서 index를 계산합니다.

import sys
N, M = map(int, input().split())
queue = [n for n in range(N)]

target = list(map(int,input().split()))

f=0

cnt = 0 

for i in range(M):
    t = target[i]-1
    f = f%len(queue)
    if(queue[f] == t):
        queue.pop(f)
    else:
        f1 = f
        c1 = 0
        f2 = f
        c2 = 0
        while(queue[f1] != t):
            f1 = (f1+1)%len(queue)
            c1 += 1
        while(queue[f2] != t):
            f2 = (f2-1+len(queue))%len(queue)
            c2 += 1
        if c1 <= c2:
            f = f1
            cnt += c1
            queue.pop(f)
        else:
            f = f2
            cnt += c2
            queue.pop(f)
print(cnt)