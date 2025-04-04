import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
ranks = [0 for _ in range(n + 1)]

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
  elif ranks[parentB] < ranks[parentA]:
    parents[parentB] = parentA
  else:
    parents[parentB] = parentA
    ranks[parentA] += 1

knows = list(map(int, input().split()))
graph = []
for _ in range(m):
  graph.append(list(map(int, input().split())))

if knows[0] == 0:
  print(m)
else:
  for i in range(1, knows[0]):
    _union(knows[i], knows[i + 1])

  for party in graph:
    for i in range(1, party[0]):
      _union(party[i], party[i + 1])

  answer = 0
  parent = _find(knows[1])
  for party in graph:
    if parent != _find(party[1]):
      answer += 1

  print(answer)