from collections import deque

n, k = map(int, input().split())

maxRange = 200_001
visit = [0] * maxRange

q = deque()
q.append(n)

while q:

  tmp = q.popleft()
  count = visit[tmp]

  if tmp == k:
    print(count)
    break
  count += 1

  if 0 <= tmp - 1 and visit[tmp - 1] == 0:
    q.append(tmp - 1)
    visit[tmp - 1] = count

  if tmp + 1 < maxRange and visit[tmp + 1] == 0:
    q.append(tmp + 1)
    visit[tmp + 1] = count

  if tmp * 2 < maxRange and visit[tmp * 2] == 0:
    q.append(tmp * 2)
    visit[tmp * 2] = count    
