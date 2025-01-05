
weight = int(input())

limit = int(weight**0.5)
answers = []

for i in range(2, limit + 1):

  while(weight % i == 0):
    answers.append(i)
    weight = weight / i

if(weight > limit):
  answers.append(int(weight))

print(len(answers))
print(*answers)