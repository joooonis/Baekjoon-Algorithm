function solution(tickets) {
    var answers = [];
    
    const usedTickets = new Array(tickets.length).fill(false)
    
    const dfs = (curret, count, path) => {
        if (count === tickets.length) {
            answers.push(path)
            return
        }
        for (let i=0; i<tickets.length; i++){
            if(tickets[i][0] === curret && !usedTickets[i]){
                usedTickets[i] = true
                dfs(tickets[i][1], count + 1, [...path, tickets[i][1]])
                usedTickets[i] = false
            }
        }
    }
    tickets.sort()
    dfs('ICN', 0, ['ICN'])
    answers.sort()
    return answers[0];
}