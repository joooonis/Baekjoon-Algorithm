function solution(n, wires) {
    const graph = Array(n+1).fill().map(()=>[])
    
    for (const [v1,v2] of wires){
        graph[v1].push(v2)
        graph[v2].push(v1)
    }

    let answer = Infinity
    for (const [v1,v2] of wires){
        const g = [...graph]
        g[v1] = g[v1].filter(v => v !== v2)
        g[v2] = g[v2].filter(v => v !== v1)
        let visited = Array(n+1).fill(false)
        let count = 0
        dfs(1, g, visited,0)
        count = visited.filter(v=>v).length
        answer = Math.min(answer, Math.abs(n - count - count))
    }
    return answer;
}

function dfs(start, graph, visited){
    visited[start] = true
    for (let next of graph[start]){
        if (!visited[next]) {
            visited[next] = true
            dfs(next, graph, visited)
        
        }
    }
    
}