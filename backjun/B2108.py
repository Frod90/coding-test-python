import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
nums = sorted(int(input()) for _ in range(n))

avg = int(round(sum(nums) / n, 0))
mid = nums[n//2]

counter = Counter(nums)
mostCom = counter.most_common()

ran = nums[-1] - nums[0]

print(avg)
print(mid)

if len(counter) > 1 and mostCom[0][1] == mostCom[1][1]:
  print(mostCom[1][0])
else:
  print(mostCom[0][0])

print(ran)