import sys
input = sys.stdin.readline

n = int(input())
values = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')
for bit in range(1, 1 << n):
  s, b = 1, 0
  for i in range(n):
    if bit & (1 << i):
      s *= values[i][0]
      b += values[i][1]
  answer = min(answer, abs(s - b))

print(answer)