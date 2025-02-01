
n, m = map(int, input().split())

arr = []

def recur(i):

  if(i == m):
    print(*arr)
    return
  
  for j in range(1, n + 1):

    arr.append(j)
    recur(i + 1)
    arr.pop()

recur(0)