from collections import deque

N, K = map(int, input().split())

maxRange = 150_001
q = deque()
q.append(N)

dist = [0] * maxRange

answer = -1
while q:

  currentX = q.popleft()

  if currentX == K:
    answer = dist[currentX]
    break

  for nx in [currentX + 1, currentX - 1, currentX * 2]:


    if 0 <= nx < maxRange and dist[nx] == 0:
      dist[nx] = dist[currentX] + 1
      q.append(nx)

print(answer)
