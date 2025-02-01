
n, m = map(int, input().split())

visit = [0 for _ in range(n + 1)]
arr = []

def recur(i):

  if i == m:
    print(*arr)
    return
  
  for j in range(1, n + 1):
    if visit[j]:
      continue

    visit[j] = 1
    arr.append(j)
    recur(i + 1)

    visit[j] = 0
    arr.pop()

recur(0)