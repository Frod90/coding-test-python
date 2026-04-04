import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

left, right = 1, 10**18
answer = -1
while left <= right:
  mid = (left + right) // 2

  count = 0
  for time in times:
    count += mid // time
  
  if count >= m:
    right = mid - 1
    answer = mid
  else:
    left = mid + 1

print(answer)