from collections import Counter

def isA(digit):
    return ord('a') <= ord(digit) <= ord('z') or ord('A') <= ord(digit) <= ord('Z')
        
def make_bigrams(string):
    tmp = []
    for i in range(len(string) - 1):
        a, b = string[i], string[i + 1]
        if isA(a) and isA(b):
            tmp.append((a + b).lower())
    return Counter(tmp)

def solution(str1, str2):
    bigrams1 = make_bigrams(str1)
    bigrams2 = make_bigrams(str2)
    if not bigrams1 and not bigrams2:
        return 65536
    
    inner = bigrams1 & bigrams2
    union = bigrams1 | bigrams2
    return int(sum(inner.values()) / sum(union.values()) * 65536)