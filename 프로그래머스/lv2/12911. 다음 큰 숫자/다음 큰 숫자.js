function solution(n) {
    const count = countOne(n)
    n++
    while (countOne(n) !== count){
        n++
    }
        
    return n;
}

const countOne = (num) => {
    let count = 0
    const bit = num.toString(2)
    bit.split('').forEach(v => {
        if(v === '1')
        count++
    })
    return count
}