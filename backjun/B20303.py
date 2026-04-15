import sys
input = sys.stdin.readline
sys.setrecursionlimit(30_001)

n, m, k = map(int, input().split())
candies = list(map(int, input().split()))
links = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  links[a].append(b)
  links[b].append(a)

def recur(current):
  count, candy = 1, candies[current]
  for next in links[current]:
    if not visit[next]:
      visit[next] = True
      next_count, next_candy = recur(next)
      count += next_count
      candy += next_candy
  return count, candy

visit = [False] * n
infos = []
for node in range(n):
  if not visit[node]:
    visit[node] = True
    count, candy = recur(node)
    infos.append((count, candy))

dists = [0] * k
for count, candy in infos:
  for i in range(k - 1, count - 1, -1):
    dists[i] = max(dists[i], dists[i - count] + candy)
print(dists[k - 1])