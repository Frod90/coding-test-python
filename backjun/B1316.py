import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for _ in range(n):

  visit = [0 for _ in range(26)]
  chars = list(input().strip())

  tmp = ''
  isAnswer = True
  for a in chars:
    
    if tmp == a:
      continue

    tmp = a
    if visit[ord(tmp) - ord('a')] != 0:
      isAnswer = False
      break
    
    visit[ord(tmp) - ord('a')] = 1
  
  if isAnswer:
    answer += 1

print(answer)