import sys
input = sys.stdin.readline

def lps(p):
  j = 0
  f = [0] * len(p)

  for i in range(1, len(p)):

    while j > 0 and p[i] != p[j]:
      j = f[j - 1]
    
    if p[i] == p[j]:
      j += 1
      f[i] = j

  return f

def kmp(text, pattern):
  j = 0
  fail = lps(p)

  count = 0
  indexs = []

  for i in range(len(text)):

    while j > 0 and text[i] != pattern[j]:
      j = fail[j - 1]

    if text[i] == pattern[j]:
      j += 1

    if j == len(pattern):
      j = fail[j - 1]
      count += 1
      indexs.append(i + 1 - len(pattern) + 1)

  return count, indexs

t = input().rstrip()
p = input().rstrip()


count, indexs = kmp(t, p)

print(count)
print(*indexs)