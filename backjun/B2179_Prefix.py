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

prefix, max_prefix_size, prefix_index = "", -1, n + 1
for i in range(n - 1):
  index1, word1 = sorted_words[i]
  index2, word2 = sorted_words[i + 1]
  
  min_index = min(index1, index2)
  prefix_size = cal(word1, word2)

  if prefix_size > max_prefix_size:
    prefix = word1[:prefix_size]
    max_prefix_size = prefix_size
    prefix_index = min_index
  elif prefix_size == max_prefix_size and min_index < prefix_index:
    prefix = word1[:prefix_size]
    prefix_index = min_index

answers = []
for word in words:
  if answers and answers[0] == word:
    continue

  if word.startswith(prefix):
    answers.append(word)

  if len(answers) >= 2:
    break

for answer in answers:
  print(answer)