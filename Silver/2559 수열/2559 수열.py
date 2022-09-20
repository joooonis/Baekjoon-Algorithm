import sys

n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))


answer = []
answer.append(sum(lst[:k]))

for i in range(n-k):
    answer.append(answer[i] - lst[i] + lst[k+i])
    
print(max(answer))
