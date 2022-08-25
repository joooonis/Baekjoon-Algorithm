n, m = map(int, input().split())
s1, s2 = [],[]
for _ in range(n):
    s1.append(input())

for _ in range(m):
    s2.append(input())

s1.sort()

ans = 0

def binarySearch(n, arr):
    left,right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == n:
            return True
        elif n > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False
        

for s in s2:
    if binarySearch(s, s1):
        ans += 1
print(ans)


import sys
N, M = map(int, input().split())
arr = dict()
cnt = 0
for _ in range(N):
    s = sys.stdin.readline()
    arr[s] = True
for _ in range(M):
    inp = sys.stdin.readline()
    if inp in arr.keys():
        cnt+=1

print(cnt)