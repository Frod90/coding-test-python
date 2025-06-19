import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[]]

for i in range(n):
  inputs = list(map(int, input().split()))
  graph.append(inputs[1:])

def _recur(cow):
  for site in graph[cow]:
    if visit[site]:
      continue

    visit[site] = True
    
    if result[site] == 0 or _recur(result[site]):
      result[site] = cow
      return True

  return False

count = 0
result = [0] * (m + 1)
for i in range(1, n + 1):
  visit = [False] * (m + 1)
  if _recur(i):
    count += 1

print(count)