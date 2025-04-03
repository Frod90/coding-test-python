import sys
input = sys.stdin.readline

k, n = map(int, input().split())
graph = [int(input()) for _ in range(k)]

mini, maxi = 0, 2**31
answers = 0

while mini <= maxi:  
  mid = (mini + maxi) // 2

  count = 0
  for length in graph:
    count += length // mid
  
  if count >= n:
    answer = mid
    mini = mid + 1
  else:
    maxi = mid - 1
  
print(answer)