import sys
sys.setrecursionlimit(99999999)

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def _recur(i, si):

  for j in range(n):
    if graph[i][j] == 1 and not visit[j]:
      visit[j] = True
      graph[si][j] = 1
      _recur(j, si)

for i in range(n):
  visit = [False for _ in range(n)]
  _recur(i, i)
  
for row in graph:
  print(*row)