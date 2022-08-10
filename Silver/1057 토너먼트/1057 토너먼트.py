n, a, b = map(int, input().split())
lst = [ n+1 for n in range(n)]
r = 1

while len(lst) != 1:
    winners = []
    for i in range(len(lst)//2*2):
        if i%2 == 0:
            x = lst[i]
            y = lst[i+1]
            if x == a and y == b:
                print(r)
            if x == b and y == a:
                print(r)
                
            if x == a:
                winners.append(x)
            elif x == b:
                winners.append(x)
            elif y == a:
                winners.append(y)
            elif y == b:
                winners.append(y)
            else:
                winners.append(lst[i])
            
    if len(lst)%2 != 0:
        winners.append(lst[-1])
    r += 1
    lst = winners
        
    
