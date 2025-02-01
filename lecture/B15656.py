
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []

def recur(i):

  if i == m:
    print(*arr)
    return
  
  for j in range(n):

    arr.append(numbers[j])
    recur(i + 1)
    arr.pop()

recur(0)