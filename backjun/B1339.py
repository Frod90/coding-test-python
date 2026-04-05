import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
words = [input().rstrip() for _ in range(n)]

scores = defaultdict(int)
for word in words:
  word_length = len(word)
  for i in range(word_length):
    scores[word[i]] += 10**(word_length - i - 1)

weights = sorted(scores.values(), reverse=True)
answer = 0
num = 9
for weight in weights:
  answer += weight * num
  num -= 1

print(answer)