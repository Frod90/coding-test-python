from collections import deque

n, k = map(int, input().split())
cores = list(map(int, input().split()))
q = deque()
visit = {}

for c in cores:
  q.append(c)
  visit[c] = 0

def _cal():
  answer = 0
  count = 0

  while q:
    bi = q.popleft()

    for ei in [1, -1]:
      ni = bi + ei
      if visit.get(ni, -1) == -1:
        visit[ni] = visit[bi] + 1
        answer += visit[ni]
        count += 1
        q.append(ni)

      if count == k:
        return answer
      
  return answer

print(_cal())