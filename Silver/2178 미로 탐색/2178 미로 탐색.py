import sys
sys.setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    line = sys.stdin.readline().rstrip()
    graph.append([i for i in line ])

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

graph[0][0] = 1
queue = [[0,0]]
    
while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if graph[nx][ny] == '1':
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1          
                            
print(graph)

    





            
