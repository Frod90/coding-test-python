
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []

def recur(i, j):

  if i == m:
    print(*arr)
    return
  
  for k in range(j, n):
    arr.append(numbers[k])
    recur(i + 1, k + 1)
    arr.pop()

recur(0, 0)
