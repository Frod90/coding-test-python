strings = input()

st = []
tmp = 1
if strings[0] == '(':
  tmp *= 2
elif strings[0] == '[':
  tmp *= 3
else:
  print(0)
  exit()
st.append(strings[0])
  
answer = 0
for i in range(1, len(strings)):
  digit = strings[i]

  if digit == '(':
    tmp *= 2
    st.append(digit)

  elif digit == '[':
    tmp *= 3
    st.append(digit)

  elif digit == ')':
    if not st or st[-1] != '(':
      answer = 0
      break
    
    if strings[i - 1] == '(':
      answer += tmp
    
    st.pop()
    tmp //= 2

  elif digit == ']':
    if not st or st[-1] != '[':
      answer = 0
      break
    
    if strings[i - 1] == '[':
      answer += tmp
    
    st.pop()
    tmp //= 3
  
print(0 if st else answer)