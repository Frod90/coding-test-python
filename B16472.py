n = int(input())
string = list(str(input()))

chars = {}
answers = []

j = 0
for i in range(len(string)):

  if string[i] in chars:
    chars[string[i]] += 1
  else:
    chars[string[i]] = 1

  while len(chars) > n:
    chars[string[j]] -= 1
    if chars[string[j]] == 0:
      del chars[string[j]]
    j += 1
  
  answers.append(i - j + 1)

print(max(answers))