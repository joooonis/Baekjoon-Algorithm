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


from collections import deque

def bfs(graph, r, visited):
    queue = deque([r])
    global count
    visited[r] = count
    
    while queue:
        v = queue.popleft()
        graph[v].sort(reverse=True)
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                count += 1
                visited[i] = count
    
bfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])
