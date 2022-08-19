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
