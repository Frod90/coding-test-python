import sys
sys.setrecursionlimit(999999999)

n, k = map(int, input().split())

weights = []
values = []

for _ in range(n):
  weight, value = map(int, input().split())
  weights.append(weight)
  values.append(value)

answers = []
def recur(i, weight, value, beforeValue):

  if i >= n:
    if weight <= k:
      answers.append(value)
    return
  
  if weight > k:
    answers.append(beforeValue)
    return

  recur(i + 1, weight + weights[i], value + values[i], value)
  recur(i + 1, weight, value, value)

recur(0, 0, 0, 0)

print(max(answers))