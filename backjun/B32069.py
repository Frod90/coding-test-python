from collections import deque

l, n, k = map(int, input().split())
idxs = list(map(int, input().split()))

q = deque()
visit = {}
for idx in idxs:
  visit[idx] = True
  q.append([0, idx])

count = 0
while q:

  bv, bi = q.popleft()
  print(bv)
  count += 1

  if count >= k:
    break

  if bi - 1 >= 0 and not visit.get(bi - 1, False):
    visit[bi - 1] = True
    q.append([bv + 1, bi - 1])
  if bi + 1 <= l and not visit.get(bi + 1, False):
    visit[bi + 1] = True
    q.append([bv + 1, bi + 1])