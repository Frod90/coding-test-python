
n, m = map(int, input().split())
arr = []

def recur(i, number):

  if i == m:
    print(*arr)
    return
  
  for j in range(number, n + 1):

    arr.append(j)
    recur(i + 1, j)
    arr.pop()

recur(0, 1)