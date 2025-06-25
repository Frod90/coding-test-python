import sys
from bisect import bisect_left
from collections import deque

input = sys.stdin.readline

m = int(input())
graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key=lambda x: x[0])

lis = []
idxs = []

for a, b in graph:
  idx = bisect_left(lis, b)
  if idx == len(lis):
    lis.append(b)
  else:
    lis[idx] = b
  idxs.append(idx)

count = len(lis) - 1
cuts = deque()
for i in range(len(idxs) - 1, -1, -1):
  if idxs[i] == count:
    count -= 1
  else:
    cuts.append(graph[i][0])

print(len(cuts))
while cuts:
  print(cuts.pop())