import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

t = int(input())
n = int(input())
nums01 = list(map(int, input().split()))
m = int(input())
nums02 = list(map(int, input().split()))

sums01 = []
for i in range(n):
  tmp = 0
  for j in range(i, n):
    tmp += nums01[j]
    sums01.append(tmp)

sums02 = []
for i in range(m):
  tmp = 0
  for j in range(i, m):
    tmp += nums02[j]
    sums02.append(tmp)
sums02.sort()

answer = 0
for sum01 in sums01:
  find_sum = t - sum01
  index = bisect_left(sums02, find_sum)
  if index < len(sums02) and sums02[index] == find_sum:
    answer += bisect_right(sums02, find_sum) - index

print(answer)