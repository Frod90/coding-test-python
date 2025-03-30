
n, m = map(int, input().split())

visit = [0 for _ in range(m + 1)]
visit[1] = 1

for i in range(2, int(m**0.5) + 1):

  if visit[i] == 0:    
    j = 2
    while i * j < m + 1:
      visit[i * j] = 1
      j += 1

for i in range(n, m + 1):
  if visit[i] == 0:
    print(i)