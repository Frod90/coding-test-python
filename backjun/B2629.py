import sys
input = sys.stdin.readline

k = int(input())
weights = list(map(int, input().split()))
n = int(input())
targets = list(map(int, input().split()))

possible = set()
for weight in weights:
  next_possible = set()
  next_possible.add(weight)
  for p in possible:
    next_possible.add(p + weight)
    next_possible.add(abs(p - weight))

  possible.update(next_possible)

answers = []
for target in targets:
  if target in possible:
    answers.append('Y')
  else:
    answers.append('N')
print(" ".join(answers))