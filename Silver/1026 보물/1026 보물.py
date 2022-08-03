N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
B.reverse()

answer = 0
for a, b in zip(A, B):
    answer += a*b
print(answer)
    
# B를 재배열 하지 않고 풀기 

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
for i in range(N):
    answer += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(answer)