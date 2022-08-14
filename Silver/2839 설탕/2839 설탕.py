# n = 5*a + 3*b
n = int(input())
a = n//5
b = n//3
lst = []
for a in range(a+1):
    for b in range(b+1):
        k = 5*a + 3*b     
        if k <= n:
            lst.append(k)
cnt = 0
pack = n
while pack > 0:
    if pack-5 in lst:
        pack -= 5
        cnt += 1
    elif pack-3 in lst:
        pack -= 3
        cnt += 1
    else:
        print(-1)
        break
if pack == 0:
    print(cnt)