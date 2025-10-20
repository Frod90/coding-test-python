import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
words = [set(input().rstrip()) for _ in range(n)]

if k < 5:
  print(0)
  exit()

base = set(['a', 'n', 't', 'i', 'c'])
extra = set()
for word in words:
  extra |= word
extra = extra - base

if k - 5 > len(extra):
  print(n)
  exit()

answer = 0
for combi in combinations(extra, k - 5):
  learn = base | set(combi)

  count = 0
  for word in words:
    if word <= learn:
      count += 1

  answer = max(answer, count)

print(answer)