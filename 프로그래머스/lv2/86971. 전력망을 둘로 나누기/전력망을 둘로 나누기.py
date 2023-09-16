def solution(n, wires):
    graph = {}

    for u,v in wires:
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]

    def dfs(i, graph, visited):
        visited.add(i)
        count = 1
        for v in graph[i]:
            if not v in visited:
                count += dfs(v, graph, visited)
        return count
    
    answer = n
    
    for u, v in wires:
        visited = set()
        graph[u].remove(v) 
        graph[v].remove(u) 
        count = dfs(1,graph,visited)
        answer = min(answer, abs(n - count - count))
        graph[u].append(v) 
        graph[v].append(u) 

    return answer