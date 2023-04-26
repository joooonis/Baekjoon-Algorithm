function solution(msg) {
    let answer = [];
    let index = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 


    for (let i=0; i<msg.length; i++){
        max = JSON.parse(JSON.stringify(index));
        max.sort((x,y) => y.length - x.length)
        k = max[0].length

        wlen = i
        w = ''
        c = ''

        for (let j=i+k; j>i; j--){
            w = msg.slice(i,j)
            c = msg.slice(j,j+1)
            if(index.indexOf(w) != -1){
            answer.push(index.indexOf(w) + 1)  
            wlen = j - i    
            index.push(w+c)        
            break
            }
        }

        i += wlen-1

    }


    return answer;
}