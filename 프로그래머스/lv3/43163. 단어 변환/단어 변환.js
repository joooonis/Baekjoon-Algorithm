function solution(begin, target, words) {
    var answer = 0;
    words.push(begin)
    const graph = Array(words.length).fill().map(()=>[])
    

    for (let i=0; i<words.length-1; i++){
        for (let j=i+1; j<words.length; j++){
            if (isConnected(words[i],words[j])){
                graph[i].push(j)
                graph[j].push(i)
            }
        }
    }
    
    const visited = Array(words.length).fill(false)

    let answers = []
    
    function dfs(node, target, count){
        visited[node] = true
        if (node === target) answers.push(count)
        for (let next of graph[node]){
            if (!visited[next]) {
                dfs(next,target,count+1)
                visited[next] = false
            }
        }
        
    }

    let start = words.indexOf(begin)
    let end = words.indexOf(target)
    dfs(start, end, 0)
    return answers.length ? Math.min(...answers) : 0;
}

const isConnected = (w1, w2) => {
    let diff = 0
    for (let i=0; i<w1.length; i++){
        if (w1[i] !== w2[i]) diff++
    }
    return diff === 1
}