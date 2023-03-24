function solution(priorities, location) {
    const queue = priorities.map((v,i)=>[v,i])    
    let count = 1
    
    while(queue.length > 0){
        paper = queue.shift()
        if (Math.max(...queue.map(v=>v[0])) > paper[0]){
            queue.push(paper)
        } else if (paper[1] === location ){
            return count
        } else {
            count++
        }
    }
    return count
}