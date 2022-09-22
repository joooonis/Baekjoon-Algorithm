import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

x = int(sys.stdin.readline())
cnt = 0

i = 0
j = n - 1

while i < j:
    if arr[i] + arr[j] == x:
        cnt += 1
        i += 1
        j -= 1
    elif arr[i] + arr[j] > x:
        j -= 1
    else:
        i += 1
   
print(cnt)
