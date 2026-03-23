import sys
input = sys.stdin.readline
sys.setrecursionlimit(200_000)

n, base, target = map(int, input().split())
links = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b, v = map(int, input().split())
  links[a].append((b, v))
  links[b].append((a, v))

def recur(current, total_dist, max_dist):
  if current == target:
    print(total_dist - max_dist)
    exit()

  for next, next_dist in links[current]:
    if not visit[next]:
      visit[next] = True
      recur(next, total_dist + next_dist, max(max_dist, next_dist))

visit = [False] * (n + 1)
visit[base] = True
recur(base, 0, 0)