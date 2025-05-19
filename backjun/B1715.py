import sys
import heapq

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]
nums.sort()
heapq.heapify(nums)

answer = 0
while len(nums) > 1:

  a, b = heapq.heappop(nums), heapq.heappop(nums)
  tmp = a + b
  answer += tmp
  heapq.heappush(nums, tmp)
  
print(answer)