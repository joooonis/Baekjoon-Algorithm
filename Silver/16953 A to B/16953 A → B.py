a, b = map(int, input().split())

cnt = 1

while b > a:
    cnt += 1
    if b%10 == 1:
        b //= 10
        
    elif b%2 == 0:
        b //= 2
    else:
        break

if a == b:
    print(cnt)
else:
    print(-1)
