import sys
n = int(input())
dice = list(map(int, input().split()))
lst = []
lst.append(min(dice[0],dice[5]))
lst.append(min(dice[1],dice[4]))
lst.append(min(dice[2],dice[3]))

lst = sorted(lst)

if n == 1:
  print(sum(sorted(dice)[0:5]))

else:
  s1 = (5*n**2 - 16*n +12)*min(lst)
  s2 = (8*n-12)*sum(lst[0:2])
  s3 = 4*sum(lst)
  print(s1 + s2 + s3)