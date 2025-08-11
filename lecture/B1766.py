import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
links = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
for _ in range(m):
  a, b = map(int, input().split())
  links[a].append(b)
  degree[b] += 1

q = []
for i in range(1, n + 1):
  if degree[i] == 0:
    q.append(i)

arr = []
while q:
  bi = heapq.heappop(q)
  arr.append(bi)

  for ni in links[bi]:
    degree[ni] -= 1
    if degree[ni] == 0:
      heapq.heappush(q, ni)

print(*arr)