import sys

sys.setrecursionlimit(99999999)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]

def _recur(x, y, l, d):

  global answer

  if l == 4:
    answer = max(d, answer)
    return

  for ex, ey in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
    nx, ny = x + ex, y + ey

    if 0 <= nx < m and 0 <= ny < n:
      if not visit[ny][nx]:
        visit[ny][nx] = True
        _recur(nx, ny, l + 1, d + graph[ny][nx])
        visit[ny][nx] = False

def _makeCorrect(x, y):
    global answer

    arms = []
    total = graph[y][x]

    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            arms.append(graph[ny][nx])
    
    if len(arms) < 3:
        return
    arms.sort(reverse=True)
    answer = max(answer, total + sum(arms[:3]))

answer = 0
for y in range(n):
  for x in range(m):
    visit[y][x] = True
    _recur(x, y, 1, graph[y][x])
    visit[y][x] = False
    _makeCorrect(x, y)

print(answer)