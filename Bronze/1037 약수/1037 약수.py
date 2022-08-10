n = int(input())
nums = sorted(list(map(int, input().split())))
if n%2 == 0:
    print(nums[0]*nums[-1])
else:
    print(nums[n//2]**2)
