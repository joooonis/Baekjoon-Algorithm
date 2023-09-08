def solution(begin, target, words):
    visited = set()
    global answer
    answer = float('inf')
    def dfs(curr,count):
        global answer
        if curr == target:
            answer = min(answer, count)
            return
        for w in words:
            if is_connect(curr, w) and w not in visited:
                visited.add(w)
                dfs(w,count+1)
                visited.pop()
                
    def is_connect(a,b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count == 1

    if target not in words:
        return 0
    dfs(begin,0)
    return answer 
                
    
