import sys
input = sys.stdin.readline
from math import isqrt

mini, maxi = map(int, input().split())

arr = [True] * (maxi - mini + 1)
for i in range(2, isqrt(maxi) + 1):
  unit = i**2
  start = ((mini + unit - 1) // unit) * unit

  for j in range(start, maxi + 1, unit):
    arr[j - mini] = False

print(arr.count(True))