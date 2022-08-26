import sys

n = int(input())
stack = []

for _ in range(n):
    w = sys.stdin.readline().split()
    order = w[0]
    if order == 'push':
        stack.append(w[1])

    elif order == 'pop':
        if not stack:
            print(-1)
        else:
            print(astack.pop())

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
