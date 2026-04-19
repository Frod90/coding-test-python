import sys
sys.stdin.readline

total_time, n = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]
dists = [0] * (total_time + 1)

for score, time in infos:
  for i in range(total_time, time - 1, -1):
    dists[i] = max(dists[i], dists[i - time] + score)

print(dists[total_time])