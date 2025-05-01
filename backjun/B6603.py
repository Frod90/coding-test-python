import sys
from itertools import combinations

input = sys.stdin.readline

while True:

  inputs = list(map(int, input().split()))

  if inputs[0] == 0:
    break

  for nums in combinations(inputs[1:inputs[0] + 1], 6):
    print(*nums)
  print()