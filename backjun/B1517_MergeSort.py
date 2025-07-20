import sys
sys.setrecursionlimit(2_000_000)
input = sys.stdin.readline

def merge_sort(s, e):
  global reversePairCount

  if s == e:
    return [nums[s]]
  
  mid = (s + e) // 2
  left = merge_sort(s, mid)
  right = merge_sort(mid + 1, e)

  merge = []
  l, r = 0, 0
  while l < len(left) and r < len(right):
    if left[l] <= right[r]:
      merge.append(left[l])
      l += 1
    else:
      merge.append(right[r])
      r += 1
      reversePairCount += len(left) - l

  merge += left[l:]
  merge += right[r:]
  return merge

n = int(input())
nums = list(map(int, input().split()))

reversePairCount = 0
merge_sort(0, n - 1)
print(reversePairCount)