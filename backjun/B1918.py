string = input().rstrip()
s = []
result = []

for digit in string:
  if digit == '(':
    s.append(digit)
  elif digit == ')':
    while s and s[-1] != '(':
      result.append(s.pop())
    s.pop()
  elif digit == '*' or digit == '/':
    while s and (s[-1] == '*' or s[-1] == '/'):
      result.append(s.pop())
    s.append(digit)
  elif digit == '+' or digit == '-':
    while s and s[-1] != '(':
      result.append(s.pop())
    s.append(digit)
  else:
    result.append(digit)

while s:
  result.append(s.pop())

print("".join(result))