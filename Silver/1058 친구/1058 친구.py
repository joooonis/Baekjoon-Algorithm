n = int(input())

# graph 초기화
graph = [[None for _ in range(n)] for _ in range(n)]

# 2차원 배열 graph 생성 
for i in range(n):
    x = input()
    for j in range(n):
        if x[j] == 'Y':
            graph[i][j] = True
        else:
            graph[i][j] = False

friend = [] 

# bfs level=2 까지 수행
for i in range(n):
    cnt = set()
    for j in range(n):
        if graph[i][j]:
            cnt.add(j)
            for k in range(n):
                if graph[j][k] and k != i:
                    cnt.add(k)
    friend.append(cnt)

print(len(max(friend, key=len)))

#안녕하세요