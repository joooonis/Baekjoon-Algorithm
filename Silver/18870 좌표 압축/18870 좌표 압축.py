import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

lst2 = sorted(list(set(lst)))

comp = dict()

for i in range(len(lst2)):
    if lst2[i] not in comp.keys():
        comp[lst2[i]] = str(i)

# comp = { lst2[i]:i for i in range(len(lst2)) }

ans = []

for i in range(len(lst)):
    ans.append(comp[lst[i]])

print(' '.join(ans))
