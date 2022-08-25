import sys
n, K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
ans,cnt = 0, 0

while ans < K:
    q = (K - ans) // coins[-1]
    if  q == 0:
        coins.pop()
    else:
        ans += coins[-1]*q
        coins.pop()
        cnt += q
    
if ans == K:
    print(cnt)
