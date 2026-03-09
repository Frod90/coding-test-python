import sys
input = sys.stdin.readline

def is_pseudo(left, right, string):
  while left < right:
    if string[left] == string[right]:
      left += 1
      right -= 1
    else:
      return False
    
  return True

t = int(input())
for _ in range(t):
  string = input().rstrip()
  n = len(string)
  left, right = 0, n - 1
  count = 0
  while left < right:
    if string[left] == string[right]:
      left += 1
      right -= 1
    else:
      if is_pseudo(left + 1, right, string) or is_pseudo(left, right - 1, string):
        count = 1
      else:
        count = 2
      
      break
  
  print(count)