def solution(numbers):
    numbers = list(map(str, numbers))
    quick_sort(numbers, 0, len(numbers)-1)
    return str(int(''.join(numbers)))

def quick_sort(numbers, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    pivot = partition(numbers, start, end) # pivot을 기준으로 분할
    quick_sort(numbers, start, pivot-1)
    quick_sort(numbers, pivot+1, end)

def partition(numbers, start, end):
    pivot = numbers[end] # 리스트의 마지막 값을 피벗으로 설정
    i = start - 1
    for j in range(start, end):
        # 두 문자열을 이어 붙였을 때 큰 값을 앞으로 오도록 비교
        if numbers[j] + pivot > pivot + numbers[j]:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[end] = numbers[end], numbers[i+1]
    return i+1
