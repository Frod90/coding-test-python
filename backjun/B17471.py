import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

n = int(input())
peoples = list(map(int, input().split()))
links = [list(map(int, input().split()))[1:] for _ in range(n)]

def validate(entry):
  entry_set = set(entry)
  visit = set()
  visit.add(entry[0])
  q = deque()
  q.append(entry[0])

  while q:
    current = q.popleft()
    for next in links[current - 1]:
      if next not in visit and next in entry_set:
        visit.add(next)
        q.append(next)

  return len(visit) == len(entry_set)

def cal(entry, rest):
  sum_a = 0
  for node in entry:
    sum_a += peoples[node - 1]
  
  sum_b = 0
  for node in rest:
    sum_b += peoples[node - 1]

  return abs(sum_a - sum_b)

arr = [i for i in range(1, n + 1)]
INF = float('inf')
answer = INF
for count in range(1, n // 2 + 1):
  for entry in combinations(arr, count):
    if not validate(entry):
      continue
    rest = [i for i in range(1, n + 1) if i not in entry]
    if not validate(rest):
      continue
    answer = min(answer, cal(entry, rest))

print(-1 if answer == INF else answer)