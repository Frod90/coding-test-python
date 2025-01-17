import sys
sys.setrecursionlimit(99999999)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[-1]*n for _ in range(n)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def recur(i, j, beforeValue):

  if i < 0 or i >= n or j < 0 or j >= n:
    return 0
  if graph[i][j] <= beforeValue:
    return 0
  if visit[i][j] != -1:
    return visit[i][j]

  visit[i][j] = max(
    recur(i + 1, j, graph[i][j]) + 1, 
    recur(i - 1, j, graph[i][j]) + 1,
    recur(i, j + 1, graph[i][j]) + 1,
    recur(i, j - 1, graph[i][j]) + 1
  )

  return visit[i][j]

answer = 0
for i in range(n):
  for j in range(n):
    if visit[i][j] == -1:
      answer = max(answer, recur(i, j, -1))

print(answer)