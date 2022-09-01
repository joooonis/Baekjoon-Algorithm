import sys
sys.setrecursionlimit(10**9)

t = int(sys.stdin.readline())

def dfs(graph, r, c):
    if r < 0 or c < 0 or r >= len(graph) or c >= len(graph[0]):
        return
    if graph[r][c] != 1: 
        return
    graph[r][c] = 0
    dfs(graph, r+1, c)
    dfs(graph, r-1, c)
    dfs(graph, r, c+1)
    dfs(graph, r, c-1)

for _ in range(t):

    m, n, k = map(int, sys.stdin.readline().split())

    graph = [ [0 for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    ans = 0
    
    for r in range(len(graph)):
        for c in range(len(graph[0])):
            if graph[r][c] == 1:
                ans += 1
                dfs(graph,r,c)
    print(ans)
    





            
