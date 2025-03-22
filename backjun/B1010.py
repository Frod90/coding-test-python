
t = int(input())

for _ in range(t):
  n, m = map(int, input().split())

  answer = 1

  count = n
  while(count > 0):
    answer *= m
    m -= 1
    count -= 1

  while(n > 0):
    answer //= n
    n -= 1

  print(answer)