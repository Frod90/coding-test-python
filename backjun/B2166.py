import sys
input = sys.stdin.readline

n = int(input())
X = [0] * n
Y = [0] * n
for i in range(n):
 X[i], Y[i]  = map(float, input().split())

area = 0
for i in range(n):
  j = (i + 1) % n
  area += X[i] * Y[j]
  area -= X[j] * Y[i]

print(round(abs(area) / 2, 1))