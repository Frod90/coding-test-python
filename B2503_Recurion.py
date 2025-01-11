import sys
sys.setrecursionlimit(99999999)


n = int(input())
hints = [list(map(int, input().split())) for _ in range(n)]

def splitNumber(number):
  a = number // 100
  b = number // 10 - a * 10
  c = number - a * 100 - b * 10
  
  return [a, b, c]

hintNumbers = [splitNumber(hints[i][0]) for i in range(n)]

def matchBallCount(number, hintIndex):

  if(hintIndex >= n):
    return True

  a, b, c = splitNumber(number)
  if a == 0 or b == 0 or c == 0:
    return False
  if a == b or b == c or a == c:
    return False

  strikeCount = hints[hintIndex][1]
  ballCount = hints[hintIndex][2]

  hintNumber = hintNumbers[hintIndex]

  if a == hintNumber[0]:
    strikeCount -= 1
  elif a in hintNumber:
    ballCount -= 1

  if b == hintNumber[1]:
    strikeCount -= 1
  elif b in hintNumber:
    ballCount -= 1

  if c == hintNumber[2]:
    strikeCount -= 1
  elif c in hintNumber:
    ballCount -= 1
  
  if strikeCount == 0 and ballCount == 0:
    return matchBallCount(number, hintIndex + 1)
  
  return False

def run(number, answer):

  if number >= 1000:
    return answer

  if(matchBallCount(number, 0)):
    answer += 1

  return run(number + 1, answer)

print(run(100, 0))