N = int(input())

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    rout = (r1 + r2)**2
    rin = (r1 - r2)**2
    d = (x1-x2)**2 + (y1-y2)**2
    if (x1, y1) == (x2, y2):
        if r1 == r2:
            print(-1)
        else:
            print(0)
            
    elif rout < d:
        print(0)
    elif rout == d:
        print(1)
    elif rout > d and rin < d:
        print(2)
    elif rin == d:
        print(1)
    else:
        print(0)
