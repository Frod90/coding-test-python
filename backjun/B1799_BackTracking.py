import sys
sys.setrecursionlimit(99999999)
input = sys.stdin.readline

def recur(index, count):
  global answer

  if index >= len(cells):
    answer = max(answer, count)
    return

  x, y = cells[index]
  if not visit01[x + y] and not visit02[x - y + n - 1]:
    visit01[x + y] = True
    visit02[x - y + n - 1] = True

    recur(index + 1, count + 1)

    visit01[x + y] = False
    visit02[x - y + n - 1] = False

  recur(index + 1, count)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visit01 = [False] * (2 * n)
visit02 = [False] * (2 * n)

cells = [[x, y] for y in range(n) for x in range(n) if graph[y][x] == 1 and (x + y) % 2 == 0]
answer = 0
recur(0, 0)
blackAnswer = answer

cells = [[x, y] for y in range(n) for x in range(n) if graph[y][x] == 1 and (x + y) % 2 == 1]
answer = 0
recur(0, 0)
whiteAnswer = answer

print(blackAnswer + whiteAnswer)