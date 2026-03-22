import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

n = int(input())
links = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b = map(int, input().split())
  links[a].append(b)
  links[b].append(a)

def recur(current):
  for next in links[current]:
    if not visit[next]:
      visit[next] = True
      recur(next)
      dists[current][0] += dists[next][1]
      dists[current][1] += min(dists[next])

dists = [[0, 1] for _ in range(n + 1)]
visit = [False] * (n + 1)
start_node = 1
visit[start_node] = True
recur(start_node)
print(min(dists[start_node]))