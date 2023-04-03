from collections import Counter
from itertools import combinations

def solution(orders, course):
    
    answer = []

    for course in course:
        entry = Counter({})
        for order in orders:
            order = sorted(list(order))
            entry += Counter(combinations(order,course))        
        
        for key, value in entry.items():
            if value == entry.most_common(1)[0][1] and value >= 2:
                answer.append(''.join(key))
        
        answer.sort()
    
    return answer