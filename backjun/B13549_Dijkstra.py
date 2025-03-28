import heapq

n, k = map(int, input().split())

maxi = 200_001
dist = [maxi for _ in range(maxi)]
q = []
heapq.heappush(q, [0, n])
dist[n] = 0

while q:

  v, x = heapq.heappop(q)

  if x == k:
    break

  if dist[x] < v:
    continue

  if 0 <= x + 1 < maxi:
    if dist[x + 1] > v:
      dist[x + 1] = dist[x] + 1
      heapq.heappush(q, [dist[x + 1], x + 1])

  if 0 <= x - 1 < maxi:
    if dist[x - 1] > v:
      dist[x - 1] = dist[x] + 1
      heapq.heappush(q, [dist[x - 1], x - 1])

  if 0 <= x * 2 < maxi:
    if dist[x * 2] > v:
      dist[x * 2] = dist[x]
      heapq.heappush(q, [dist[x * 2], x * 2])

print(dist[k])