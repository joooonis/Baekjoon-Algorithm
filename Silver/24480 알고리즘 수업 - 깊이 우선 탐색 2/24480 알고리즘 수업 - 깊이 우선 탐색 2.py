from audioop import reverse
import sys
sys.setrecursionlimit(10**9)

n, m, r = map(int, sys.stdin.readline().split())

graph = { n:[] for n in range(1,n+1) }

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


visited = [ 0 ] * (n + 1)
count = 1


def dfs(graph, v, visited):
    global count
    visited[v] = count
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(graph, i, visited)
    
dfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])
