n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
for _ in range(n):
    print(lst.pop(0))
