import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for x in data[1:]:
        graph[i].append(x - 1)

def _recur(i):
  if visit[i]:
    return False
  visit[i] = True

  for w in graph[i]:
    if result[w] == -1:
      result[w] = i
      return True

  for w in graph[i]:
    if _recur(result[w]):
      result[w] = i
      return True

  return False

count = 0
result = [-1] * m
for i in range(n):
  visit = [False] * n
  if _recur(i):
    count += 1  
  visit = [False] * n
  if _recur(i):
    count += 1

  if count == m:
    break

print(count)