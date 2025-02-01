
n = int(input())

list = [int(input()) for _ in range(n)]

for i in range(len(list)):
  number = list[i]
  isCorrect = True

  for j in range(2, 10**6):
    if(number % j == 0):
      isCorrect = False
      break

  if(isCorrect):
    print("YES")
  else:
    print("NO")

