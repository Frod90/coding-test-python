import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
words = [set(input().rstrip()) for _ in range(n)]

if k < 5:
    print(0)
    exit()

c = ord('a')
base = [ord('a') - c, ord('n') - c, ord('t') - c, ord('i') - c, ord('c') - c]
extra = [i for i in range(1, ord('z') - c + 1) if i not in base]

word_bits = []
for word in words:
    word_bit = 0
    for digit in word:
        word_bit |= (1 << (ord(digit) - c))
    word_bits.append(word_bit)

base_bit = 0
for b in base:
    base_bit |= (1 << b)

answer = 0
for combi in combinations(extra, k - 5):
    learn_bit = base_bit
    for digit in combi:
        learn_bit |= (1 << digit)

    count = 0
    for word_bit in word_bits:
        if (learn_bit & word_bit) == word_bit:
            count += 1
    answer = max(answer, count)

print(answer)