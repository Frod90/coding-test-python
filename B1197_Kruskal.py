import sys
sys.setrecursionlimit(9999999)
input = sys.stdin.readline

import heapq

V, E = map(int, input().split())
parents = [i for i in range(V + 1)]
ranks = [0] * (V + 1)

def _find(a):

  if a == parents[a]:
    return a

  parents[a] = _find(parents[a])
  return parents[a]

def _union(a, b):

  parentA, parentB = _find(a), _find(b)

  if parentA == parentB:
    return
  
  if ranks[parentA] < ranks[parentB]:
    parents[parentA] = parentB
  elif ranks[parentA] > ranks[parentB]:
    parents[parentB] = parentA
  elif ranks[parentA] == ranks[parentB]:
    parents[parentB] = parentA
    ranks[parentA] += 1

q = []

for _ in range(E):
  a, b, c = map(int, input().split())
  heapq.heappush(q, [c, a, b])


count = 1
answer = 0

while q:

  if count == V:
    break

  value, a, b = heapq.heappop(q)

  if _find(a) == _find(b):
    continue

  answer += value
  count += 1
  _union(a, b)

print(answer)