def solution(numbers):
    numbers = list(map(str, numbers)) # 숫자들을 문자열로 변환
    numbers.sort(key=lambda x: x*3, reverse=True) # 문자열을 이어 붙인 후 큰 순서대로 정렬
    return str(int(''.join(numbers))) # 0이 여러 개인 경우를 대비하여 int로 변환한 후 다시 str로 변환
