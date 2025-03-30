
n, m = map(int, input().split())

def calc(num):

  if num == 1:
    return False

  for i in range(2, int(num**(0.5)) + 1):
    if num % i == 0:
      return False
  
  return True

for num in range(n, m + 1):
  if calc(num):
    print(num)