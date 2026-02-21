import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

w = len(a)
h = len(b)
dist = [0] * (w + 1)
answer = 0

for y in range(1, h + 1):
  for x in range(w, 0, -1):
    if b[y - 1] == a[x - 1]:
      dist[x] = dist[x - 1] + 1
      answer = max(answer, dist[x])
    else:
      dist[x] = 0

print(answer)