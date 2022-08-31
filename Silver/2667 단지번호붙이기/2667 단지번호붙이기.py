import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())

graph = []

for _ in range(n):
    line = sys.stdin.readline().rstrip()
    graph.append([i for i in line ])
                 
visited = [ 0 ] * (n + 1)
count = 1


def dfs(graph, r, c):
    global count
    if r < 0 or c < 0 or r >= len(graph) or c >= len(graph[0]):
        return
    if graph[r][c] != '1': 
        return
    count += 1
    graph[r][c] = '0'
    dfs(graph, r+1, c)
    dfs(graph, r-1, c)
    dfs(graph, r, c+1)
    dfs(graph, r, c-1)

ans, counts = 0, []
for r in range(len(graph)):
    for c in range(len(graph[0])):
        if graph[r][c] == '1':
            ans += 1
            count = 0
            dfs(graph,r,c)
            counts.append(count)
            

counts.sort()

print(ans)
for count in counts:
    print(count)
