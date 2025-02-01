
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []
visit = [0 for _ in range(n)]

def recur(i):

  if i == m:
    print(*arr)
    return
  
  for j in range(n):
    
    if visit[j]:
      continue

    visit[j] = 1
    arr.append(numbers[j])
    recur(i + 1)

    visit[j] = 0
    arr.pop()

recur(0)