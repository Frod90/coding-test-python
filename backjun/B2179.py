import sys
input = sys.stdin.readline

def cal(a, b):
  if a == b:
    return -1
  
  size = min(len(a), len(b))
  for i in range(size):
    if a[i] != b[i]:
      return i
    
  return size

n = int(input())
words = [input().rstrip() for _ in range(n)]
sorted_words = sorted(enumerate(words), key=lambda x:(x[1], x[0]))

max_count = -1
s_index, s = n + 1, ""
t_index, t = n + 1, ""
for i in range(n - 1):
  base_index, base_word = sorted_words[i]

  for j in range(i + 1, n):
    compare_index, compare_word = sorted_words[j]
    compare_count = cal(base_word, compare_word)
    if compare_count == -1:
      continue

    if max_count < compare_count:
      max_count = compare_count
      if base_index < compare_index:
        s, s_index = base_word, base_index
        t, t_index = compare_word, compare_index
      else:
        s, s_index = compare_word, compare_index
        t, t_index = base_word, base_index
    
    elif max_count == compare_count:
      if base_index < s_index or compare_index < s_index:
        if base_index < compare_index:
          s, s_index = base_word, base_index
          t, t_index = compare_word, compare_index
        else:
          s, s_index = compare_word, compare_index
          t, t_index = base_word, base_index
      elif base_index == s_index and compare_index < t_index:
        t_index = compare_index
        t = compare_word
      elif compare_index == s_index and base_index < t_index:
        t_index = base_index
        t = base_word

    else:
      break

print(s)
print(t)