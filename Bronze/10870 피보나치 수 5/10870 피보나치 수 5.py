n = int(input())

def fibonacci(n):
  # base case
  if n == 0:
    return 0
  elif n == 1:
    return 1
    
  # recursion
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))