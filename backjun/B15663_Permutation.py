from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for permu in sorted(set(permutations(nums, m))):
  print(*permu)
