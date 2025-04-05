import sys
input = sys.stdin.readline

sys.setrecursionlimit(99099999)

n = int(input())

def _find(graph, a):

  if a == graph[a]:
    return a
  
  graph[a] = _find(graph, graph[a])
  return graph[a]

def _union(graph, ranks, counts, a, b):

  parentA, parentB = _find(graph, a), _find(graph, b)

  if parentA == parentB:
    return

  rankA, rankB = ranks[parentA], ranks[parentB]

  if rankA < rankB:
    graph[parentA] = parentB
    counts[parentB] += counts[parentA]
  elif rankB < rankA:
    graph[parentB] = parentA
    counts[parentA] += counts[parentB]
  else:
    graph[parentB] = parentA
    counts[parentA] += counts[parentB]
    ranks[parentA] = rankA + 1

for _ in range(n):

  m = int(int(input()))

  graph = {}
  ranks = {}
  counts = {}

  for _ in range(m):
    a, b = map(str, input().split())

    if a not in graph:
      graph[a] = a
      ranks[a] = 0
      counts[a] = 1
    
    if b not in graph:
      graph[b] = b
      ranks[b] = 0
      counts[b] = 1

    _union(graph, ranks, counts, a, b)

    count = counts[_find(graph, a)]
    print(count)