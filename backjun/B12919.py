import sys
input = sys.stdin.readline

def reverse(s):
  arr = list(s)
  n = len(s)
  for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
  return "".join(arr)

def recur(s, t):
  global answer
  if len(s) == len(t):
    if s == t:
      answer = 1
    return

  if t[-1] == 'A':
    recur(s, t[:-1])
  
  if t[0] == 'B':
    recur(s, reverse(t[1:]))
    
s = input().rstrip()
t = input().rstrip()
answer = 0
recur(s, t)
print(answer)