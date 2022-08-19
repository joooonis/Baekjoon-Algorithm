import sys
n, m = map(int, input().split())
s1, s2 = set(), set()


s1 = set(sys.stdin.readline().split())
s2 = set(sys.stdin.readline().split())


print(len(s1 | s2) - len(s1 & s2))

