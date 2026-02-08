import sys
sys.setrecursionlimit(100_000)

def is_prime(num):
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def recur(num, length):
  if length == n:
    print(num)
    return
  
  for digit in [1, 3, 7, 9]:
    next = num * 10 + digit
    if is_prime(next):
      recur(next, length + 1)

n = int(input())
for num in [2, 3, 5, 7]:
  recur(num, 1)