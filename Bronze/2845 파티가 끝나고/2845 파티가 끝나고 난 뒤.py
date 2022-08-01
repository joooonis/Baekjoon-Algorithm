L, P = map(int,input().split())
news = list(map(int,input().split()))
for n in news:
    print(n-L*P,end=' ')
