import sys

t = int(sys.stdin.readline())

for _ in range(t):
    stack = []
    ps = sys.stdin.readline().rstrip()
    for p in ps:
        if not stack:
            stack.append(p)
        elif stack[-1] =='(' and p == ')':
            stack.pop()
        else:
            stack.append(p)
    if not stack:
        print('YES')
    else:
        print('NO')
