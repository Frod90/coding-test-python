
n = int(input())
hints = []

for i in range(n):
  question, strike, ball = list(map(int, input().split()))
  hints.append([question, strike, ball])

answer = 0

for a in range(1, 10):
  for b in range(1, 10):
    for c in range(1, 10):

      if(a == b or a == c or b == c):
        continue

      count = 0
      for hint, strike, ball in hints:

         strikeCount = 0
         ballCount = 0

         check = list(str(hint))
         if(a == int(check[0])):
           strikeCount += 1
         if(b == int(check[0]) or c == int(check[0])):
           ballCount += 1

         if(b == int(check[1])):
           strikeCount += 1
         if(a == int(check[1]) or c == int(check[1])):
           ballCount += 1

         if(c == int(check[2])):
           strikeCount += 1
         if(a == int(check[2]) or b == int(check[2])):
           ballCount += 1

         if(strike == strikeCount and ball == ballCount):
           count += 1

      if(count == n):
         answer += 1

print(answer)