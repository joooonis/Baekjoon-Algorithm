import sys
input = sys.stdin.readline

x, y = map(int, input().rsplit())
z = y * 100 // x
left, right = 1, x 
answer = sys.maxsize


while left <= right:
    mid = (left + right) // 2
    w = (y + mid) * 100 // (x + mid)
    if w <= z:
        left = mid + 1
    else:
        answer = min(answer, mid)
        right = mid - 1

if z >= 99:
    print(-1)
else:
    print(answer)