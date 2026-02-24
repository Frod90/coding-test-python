import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

if n == 1:
  print(sum(nums) - max(nums))
  exit()

opposite  = [(i, 5 - i) for i in range(3)]
candidates = [min(nums[a], nums[b]) for a, b in opposite]
candidates.sort()

one_side = candidates[0]
two_side = candidates[0] + candidates[1]
three_side = sum(candidates)

one_side_count = (n - 2) * (n - 1) * 4 + (n - 2) * (n - 2)
two_side_count = (n - 1) * 4 + (n - 2) * 4
three_side_count = 4

answer = one_side * one_side_count + two_side * two_side_count + three_side * three_side_count
print(answer)