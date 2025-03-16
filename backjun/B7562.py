from collections import deque

n = int(input())

for _ in range(n):

  I = int(input())
  initX, initY = map(int, input().split())
  targetX, targetY = map(int, input().split())

  dist = [[0 for _ in range(I)] for _ in range(I)]

  q = deque()
  dist[initY][initX] = 1
  q.append([initX, initY])


  answer = -1
  while q:

    currentX, currentY = q.popleft()

    if currentX == targetX and currentY == targetY:
      answer = dist[currentY][currentX]
      break

    for ex, ey in [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]:
      nx, ny = currentX + ex, currentY + ey

      if 0 <= nx < I and 0 <= ny < I:
        if dist[ny][nx] == 0:
          dist[ny][nx] = dist[currentY][currentX] + 1
          q.append([nx, ny])

  print(answer - 1)
