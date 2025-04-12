import sys
sys.setrecursionlimit(99999999)

n = int(input())
nums = list(map(int, input().split()))
operatorsCount = list(map(int, input().split()))

answers = []

def _recur(i, r):

  if i == n:
    answers.append(r)
    return

  if operatorsCount[0] > 0:
    operatorsCount[0] -= 1
    _recur(i + 1, r + nums[i])
    operatorsCount[0] += 1
  
  if operatorsCount[1] > 0:
    operatorsCount[1] -= 1
    _recur(i + 1, r - nums[i])
    operatorsCount[1] += 1
  
  if operatorsCount[2] > 0:
    operatorsCount[2] -= 1
    _recur(i + 1, r * nums[i])
    operatorsCount[2] += 1
  
  if operatorsCount[3] > 0:
    operatorsCount[3] -= 1
    _recur(i + 1, int(r / nums[i]))
    operatorsCount[3] += 1

_recur(1, nums[0])
print(max(answers))
print(min(answers))