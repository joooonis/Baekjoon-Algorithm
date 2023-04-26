from itertools import permutations

def solution(expression):
    
    operator = []
    
    # 연산자의 위치 찾기 
    for i in range(len(expression)):
        if expression[i] in ['+','-','*']:
            operator.append(expression[i])
    
    operator_all = list(set(operator))
    
    # 숫자만 분리 
    nums = expression.replace('-','+').replace('*','+').split('+')
    
    # 가능한 우선순위 경우의 수 
    prior = list(permutations(operator_all,len(operator_all)))
    prior = [list(k) for k in prior]

    # 우선순위가 낮은 연산부터 쭉 저장     
    lst = []
    
    for p in prior:
        op = list(operator)
        numbers = list(nums)
        for i in range(len(p)):
            target = p.pop()
            while target in op:    
                tg = op.index(target)
                numbers[tg] = str(eval(numbers[tg]+op[tg]+numbers[tg+1]))
                del numbers[tg+1]
                del op[tg]
        lst.append(abs(int(numbers[0])))

    
    return max(lst)