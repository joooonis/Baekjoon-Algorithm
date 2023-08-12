function solution(priorities, location) {
  let answer = 1
  let q = priorities.map((priority,index)=>({priority,index}))
  
  while (q.length > 0){
    let p = q.shift()
    if (q.some(v => v.priority > p.priority)){
        q.push(p)
    } else {
        if (p.index === location) return answer
        else answer += 1
    } }
}