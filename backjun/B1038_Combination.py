from itertools import combinations

answers = []
nums = [i for i in range(10)]

for i in range(1, 11):

  for combi in combinations(nums, i):
    tmp = list(map(str, combi))
    tmp.sort(reverse=True)
    answers.append(int("".join(tmp)))

answers.sort()

n = int(input())
if n >= len(answers):
  print(-1)
else:
  print(answers[n])