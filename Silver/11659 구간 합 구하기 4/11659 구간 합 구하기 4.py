import sys

n, m = map(int, sys.stdin.readline().split())
prefix_sum = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i]

prefix_sum.insert(0,0)

for _ in range(m):
    i, j = map(int, sys.stdin.readline())
    print(prefix_sum[j]-prefix_sum[i-1])
