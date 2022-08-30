import sys

n = int(sys.stdin.readline())

k = int(sys.stdin.readline())

edges = []

for _ in range(k):
    edges.append(sys.stdin.readline().split())

graph = { i:[] for i in range(n) }

for edge in edges:
    graph[int(edge[0])-1].append(int(edge[1])-1)
    graph[int(edge[1])-1].append(int(edge[0])-1)

visited = [ False ] * n

'''
graph = {
    0: [1, 4], 
    1: [0, 2, 4], 
    2: [1], 
    3: [6], 
    4: [0, 1, 5], 
    5: [4], 
    6: [3]
    }
'''

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 0, visited)

print(visited.count(True)-1)

