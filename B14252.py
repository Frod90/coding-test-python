
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

def _gcd(a, b):
  while(b % a != 0):
    gap = b % a
    b = a
    a = gap

  return a

answer = 0

for i in range(len(numbers) - 1):

  a = numbers[i]
  b = numbers[i + 1]

  if(_gcd(a, b) == 1):
    continue

  answer += 1

  for newNumber in range(a, b):
    if(_gcd(a, newNumber) == 1 and _gcd(newNumber, b) == 1):
      break

    if(newNumber == b - 1):
      answer += 1

print(answer)