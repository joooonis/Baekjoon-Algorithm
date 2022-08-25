import sys
from collections import Counter

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()

print(round(sum(lst)/len(lst)))

n = len(lst)
if n%2 == 0:
    print((lst[n//2]+lst[n//2-1])/2)
else:
    print(lst[(n-1)//2])

x = Counter(lst)
most = max(x.values())
max_list = []
for key, value in x.items():
    if value == most:
        max_list.append(key)
if len(max_list) == 1:
    print(max_list[0])
else:
    print(max_list[1])

print(max(lst)-min(lst))
