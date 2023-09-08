def solution(N, number):
    # N을 사용해서 만들 수 있는 수들을 저장할 리스트를 생성합니다.
    possible_numbers = [set() for _ in range(9)]
    
    # 각 숫자를 N으로 연달아 만들 수 있는 경우를 초기화합니다.
    for i in range(1, 9):
        possible_numbers[i].add(int(str(N) * i))
    
    # 다이나믹 프로그래밍을 통해 주어진 숫자 number를 만들 수 있는 경우를 찾습니다.
    for i in range(1, 9):
        for j in range(1, i):
            for num1 in possible_numbers[j]:
                for num2 in possible_numbers[i - j]:
                    possible_numbers[i].add(num1 + num2)
                    possible_numbers[i].add(num1 - num2)
                    possible_numbers[i].add(num1 * num2)
                    if num2 != 0:
                        possible_numbers[i].add(num1 // num2)
        
        # 주어진 숫자 number를 만들 수 있다면, 사용한 숫자의 최솟값을 반환합니다.
        if number in possible_numbers[i]:
            return i
    return -1