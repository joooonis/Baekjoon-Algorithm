import sys

n = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

ans = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)
    
print(ans)

# O(n^2) 시간 초과 
for i in range(len(lst)):
    booleanFlag = True 
    for j in range(i+1,len(lst)):
        if lst[j] > lst[i]:
            print(lst[j], end=' ')
            booleanFlag = False
            break
    if booleanFlag:
        print(-1, end=' ')

