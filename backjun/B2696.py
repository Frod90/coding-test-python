import sys
input = sys.stdin.readline
import heapq

t = int(input())

for _ in range(t):
  n = int(input())
  nums = []
  for _ in range(n//10 + 1):
    nums.extend(list(map(int, input().split())))

  lower_q = []
  upper_q = []
  answers = []
  
  for i, num in enumerate(nums):
    heapq.heappush(lower_q, -num)
    if i % 2 == 1:
      continue

    while upper_q and upper_q[0] < -lower_q[0]:
      heapq.heappush(lower_q, -heapq.heappop(upper_q))

    target_size = i//2 + 1
    while len(lower_q) > target_size:
      heapq.heappush(upper_q, -heapq.heappop(lower_q))

    answers.append(-lower_q[0])

  answer_size = len(answers)
  print(answer_size)

  for left in range(0, answer_size, 10):
    right = min(left + 10, answer_size)
    print(*answers[left:right])