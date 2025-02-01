
n = int(input())

numbers = list(map(int, input().split()))

answer = 0

for number in numbers:

  if(number == 1):
    continue

  isMinority = True
  for i in range(2, number):
    if(number % i == 0):
      isMinority = False
      break

  if(isMinority):
    answer += 1

print(answer)